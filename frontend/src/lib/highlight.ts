import type { HighlighterGeneric } from "shiki";

/**
 * Syntax highlighting for code shown on notes pages.
 *
 * Ported from the React harness, where it ran on the server. Here it runs in
 * the browser, so the highlighter is imported lazily (Shiki is the largest
 * thing on these pages) and created once per tab.
 *
 * One dark theme: the code figure is always dark regardless of page theme.
 */
const THEME = "github-dark";
const LANGS = ["vue", "ts", "tsx", "python", "csharp", "xml", "bash", "css", "json", "md"] as const;
type SupportedLang = (typeof LANGS)[number];

// eslint-disable-next-line @typescript-eslint/no-explicit-any
let highlighterPromise: Promise<HighlighterGeneric<any, any>> | null = null;

function getHighlighter() {
  highlighterPromise ??= import("shiki").then(({ createHighlighter }) =>
    createHighlighter({ themes: [THEME], langs: [...LANGS] }),
  );
  return highlighterPromise;
}

function isSupported(lang: string): lang is SupportedLang {
  return (LANGS as readonly string[]).includes(lang);
}

/** Highlighted HTML, or `null` → the caller renders plain text. */
export async function highlight(code: string, lang: string): Promise<string | null> {
  if (!isSupported(lang)) return null;
  try {
    const highlighter = await getHighlighter();
    return highlighter.codeToHtml(code, { lang, theme: THEME });
  } catch {
    return null;
  }
}
