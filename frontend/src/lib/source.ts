/**
 * Real files from this repository, so a notes page can show its own
 * implementation verbatim.
 *
 * The point is comparability: the code shown next to a doc link has to be the
 * code that actually runs, not a re-typed approximation of it. The React
 * harness read files off disk in server components; a Vite app has no server
 * render, so the same guarantee comes from `import.meta.glob(..., '?raw')` —
 * Vite inlines each file's text at build time and hot-reloads it in dev, so
 * what appears is always what is on disk.
 *
 * Keys are repo-relative paths, e.g. `backend/server.ts` or
 * `frontend/src/routes/frontend-tools/demo-chat/App.vue`, or `agent/Program.cs` (the
 * MS Agent Framework agent project).
 */

const frontendFiles = import.meta.glob(
  [
    "/src/routes/**/*.{vue,ts,css}",
    "/src/components/harness/HarnessProvider.vue",
    "/src/main.ts",
    "/vite.config.ts",
    "/package.json",
  ],
  { query: "?raw", import: "default", eager: true },
) as Record<string, string>;

const backendFiles = import.meta.glob(
  [
    "../../../backend/*.ts",
    "../../../backend/runtimes/*.ts",
    "../../../backend/package.json",
    "../../../agent/*.cs",
    "../../../agent/*.csproj",
  ],
  { query: "?raw", import: "default", eager: true },
) as Record<string, string>;

const FILES: Record<string, string> = {};
for (const [key, text] of Object.entries(frontendFiles)) FILES[`frontend${key}`] = text;
for (const [key, text] of Object.entries(backendFiles)) FILES[key.replace(/^(\.\.\/)+/, "")] = text;

export interface SourceFile {
  path: string;
  code: string;
  language: string;
  lineRange?: { start: number; end: number };
  error?: string;
}

export function languageFor(file: string): string {
  if (file.endsWith(".vue")) return "vue";
  if (file.endsWith(".tsx")) return "tsx";
  if (file.endsWith(".ts")) return "ts";
  if (file.endsWith(".py")) return "python";
  if (file.endsWith(".cs")) return "csharp"; // [harness] .NET agent
  if (file.endsWith(".csproj")) return "xml";
  if (file.endsWith(".css")) return "css";
  if (file.endsWith(".json")) return "json";
  if (file.endsWith(".md")) return "md";
  return "text";
}

function escapeRe(value: string): string {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

/**
 * @param repoRelative  e.g. "backend/server.ts".
 * @param region        Optional `#region <name>` marker to slice out.
 */
export function readSource(repoRelative: string, region?: string): SourceFile {
  const language = languageFor(repoRelative);
  const raw = FILES[repoRelative];

  if (raw === undefined) {
    return {
      path: repoRelative,
      code: "",
      language,
      error: `Could not read ${repoRelative}: not in the source glob (src/lib/source.ts).`,
    };
  }

  if (!region) return { path: repoRelative, code: raw.trimEnd(), language };

  const lines = raw.split("\n");
  const startRe = new RegExp(`#\\s?region\\s+${escapeRe(region)}\\b`);
  const endRe = /#\s?endregion\b/;
  const startIdx = lines.findIndex((l) => startRe.test(l));
  if (startIdx === -1) {
    return {
      path: repoRelative,
      code: raw.trimEnd(),
      language,
      error: `Region "${region}" not found — showing the whole file.`,
    };
  }
  const rest = lines.slice(startIdx + 1);
  const endOffset = rest.findIndex((l) => endRe.test(l));
  const body = endOffset === -1 ? rest : rest.slice(0, endOffset);
  return {
    path: repoRelative,
    code: body.join("\n").replace(/^\n+|\s+$/g, ""),
    language,
    lineRange: {
      start: startIdx + 2,
      end: startIdx + 1 + (endOffset === -1 ? rest.length : endOffset),
    },
  };
}
