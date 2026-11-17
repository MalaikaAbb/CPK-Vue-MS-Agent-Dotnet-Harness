"""
[harness] Builds the code-block catalog that write-doc-files.py reads.

For every page in ../doc-snapshot/pages/ (the .md exports /doc-sync stores):
  1. extract each fenced block, dedent it, strip `[!code highlight]` markers
     (the rendered page strips them too). A leading path comment such as
     `# src/agents/foo.py` becomes the block's title, which is what the
     rendered page does with it;
  2. fetch the RENDERED page and flag each block `rendered` if its code
     appears there (whitespace-insensitive) — in a <pre>, or in a block's
     `data-raw-code` (which also covers tabs rendered client-side).

Two rules for the framework root page (/vue/<framework>), which is a landing
page in the rendered docs while its .md is the Vue Quickstart:
  - its .md blocks are checked against the rendered Vue Quickstart at /vue —
    the page the landing page's .md defers to for "the Vue frontend steps";
  - code shown on the rendered landing page but absent from the .md (the
    LangGraphAgent runtime route) is appended as extra blocks titled
    "landing: …", flagged rendered.

Usage: python3 -I scripts/build-doc-catalog.py <out.json>
"""
import glob, html, json, os, re, sys, textwrap, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(HERE, "..", "..", "doc-snapshot", "pages")


def norm(s):
    return re.sub(r"\s+", "", s)


def fetch(url):
    req = urllib.request.Request(url, headers={"user-agent": "copilotkit-harness-doc-catalog"})
    return urllib.request.urlopen(req, timeout=20).read().decode("utf-8")


def raw_code_blocks(page):
    """Exact source of every rendered code block, including blocks in tabs the
    page renders client-side: Shiki blocks carry it in `data-raw-code`, both as
    an HTML attribute and inside the page's RSC payload."""
    out = [html.unescape(v) for v in re.findall(r'data-raw-code="([^"]*)"', page)]
    def decode(chunk):
        try:
            return json.loads('"' + chunk + '"')
        except ValueError:
            return ""          # a chunk the non-greedy split cut short; others still decode
    rsc = "".join(decode(c) for c in re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', page, re.S))
    for v in re.findall(r'"data-raw-code":"((?:\\.|[^"\\])*)"', rsc):
        out.append(decode(v))
    # Long blocks are not inlined in data-raw-code: the payload carries them as
    # separate text chunks (`68:T7a6,<raw text>`) that the block references
    # ("$68"). Include the whole decoded payload so those count as rendered.
    out.append(rsc)
    # The raw source keeps `[!code highlight]` markers that the visible block
    # (and the .md extraction below) drop; strip them before comparing.
    return [re.sub(r"(//|#|<!--|\{/\*) \[!code [^\]]*\]( -->| \*/\})?", "", r) for r in out]


def rendered_blocks(page):
    out = []
    for block in re.findall(r"<pre[^>]*>(.*?)</pre>", page, re.S):
        lines = re.findall(r'<span class="line"[^>]*>(.*?)</span>\s*(?=<span class="line"|</code>)', block, re.S)
        text = "\n".join(html.unescape(re.sub(r"<[^>]+>", "", l)) for l in lines) if lines \
            else html.unescape(re.sub(r"<[^>]+>", "", block))
        out.append(text)
    return out


catalog = {}
pages = sorted(glob.glob(os.path.join(PAGES, "*.md")))
root_slug = min((os.path.basename(p)[:-3] for p in pages), key=len)          # vue__langgraph-python
framework = root_slug.split("__")[1]                                          # langgraph-python

# One extra source, not a Vue page: the framework's own Quickstart, which the
# Vue landing page links as its guide ("guideLink": "/<framework>/quickstart").
# It publishes the `sample_agent` graph and langgraph.json that the landing
# page's runtime route (graphId "sample_agent") connects to. It is fetched live
# (both .md and rendered) rather than stored in doc-snapshot/, which tracks the
# Vue sidebar pages only.
EXTRA = {"framework-quickstart": f"https://docs.copilotkit.ai/{framework}/quickstart"}
extra_dir = os.path.join(HERE, "..", "node_modules", ".tmp", "extra-pages")
os.makedirs(extra_dir, exist_ok=True)
extra_files = []
for key, url in EXTRA.items():
    path = os.path.join(extra_dir, key + ".md")
    open(path, "w").write(fetch(url + ".md"))
    extra_files.append((path, key, url))

sources = [(md, None, None) for md in pages] + extra_files
for md, extra_key, extra_url in sources:
    slug = os.path.basename(md)[:-3]
    is_root = extra_key is None and slug == root_slug
    key = extra_key or ("index" if is_root else slug.removeprefix(root_slug + "__"))
    url = extra_url or "https://docs.copilotkit.ai/" + slug.replace("__", "/")
    page_html = fetch(url)
    page_blocks = rendered_blocks(page_html)
    rendered = norm("\n".join(page_blocks + raw_code_blocks(page_html)))
    if is_root:
        rendered += norm("\n".join(rendered_blocks(fetch("https://docs.copilotkit.ai/vue"))))
    lines = open(md).read().split("\n")
    blocks, i = [], 0
    while i < len(lines):
        m = re.match(r"^(\s*)(`{3,}|~{3,})(\S*)\s*(.*)$", lines[i])   # backtick AND tilde fences
        if m:
            _, fence, lang, meta = m.groups()
            t = re.search(r'title="([^"]*)"', meta)
            body = []
            i += 1
            while i < len(lines) and not re.match(r"^\s*" + fence + r"\s*$", lines[i]):
                body.append(lines[i])
                i += 1
            code = textwrap.dedent("\n".join(body))
            code = re.sub(r"[ \t]*<!-- \[!code [^\]]*\] -->\n", "", code)
            code = re.sub(r"[ \t]*// \[!code [^\]]*\]", "", code)
            code = re.sub(r"[ \t]*# \[!code [^\]]*\]", "", code)
            code = re.sub(r"[ \t]*\{/\* \[!code [^\]]*\] \*/\}", "", code)
            title = t.group(1) if t else None
            first = code.split("\n", 1)
            pm = re.match(r"^(?:#|//)\s*((?:src|app|agent|backend)/\S+\.(?:py|ts|tsx|json|cs))\s*$", first[0])  # .cs: [harness] .NET pages
            if pm and len(first) > 1:
                title = title or pm.group(1)
                code = first[1]
            blocks.append({"lang": lang, "title": title,
                           "code": code, "rendered": norm(code) in rendered})
        i += 1
    if is_root:
        md_norm = norm("\n".join(b["code"] for b in blocks))
        for n, text in enumerate(page_blocks):
            if norm(text) and norm(text) not in md_norm:
                lang = "ts" if re.search(r"^\s*(import|export|const) ", text, re.M) else "text"
                blocks.append({"lang": lang, "title": f"landing: rendered block {n}",
                               "code": text.strip("\n") + "\n", "rendered": True})
    catalog[key] = blocks
    print(f"{key}: {len(blocks)} blocks, {sum(not b['rendered'] for b in blocks)} not on the rendered page")

json.dump(catalog, open(sys.argv[1], "w"), indent=1)
