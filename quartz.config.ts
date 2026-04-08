// Quartz 4 Configuration for MBA Second Brain
// Full docs: https://quartz.jzhao.xyz/configuration

import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "🎓 MBA Second Brain",
    pageTitleSuffix: " | MBA Knowledge Base",
    enableSPA: true,
    enablePopovers: true,
    analytics: {
      provider: "plausible",
    },
    locale: "en-US",
    baseUrl: "your-github-username.github.io/mba-brain",  // ← UPDATE THIS
    ignorePatterns: [
      "private",
      "Templates",
      ".obsidian",
      "_Assets",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Outfit",
        body: "Inter",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#fafafa",
          lightgray: "#e5e5e5",
          gray: "#b8b8b8",
          darkgray: "#4e4e4e",
          dark: "#1a1a2e",
          secondary: "#2563eb",     // Blue accent
          tertiary: "#7c3aed",      // Purple
          highlight: "rgba(37, 99, 235, 0.08)",
          textHighlight: "#fff23688",
        },
        darkMode: {
          light: "#0f172a",         // Dark navy background
          lightgray: "#1e293b",
          gray: "#475569",
          darkgray: "#94a3b8",
          dark: "#f1f5f9",
          secondary: "#60a5fa",     // Blue accent (lighter for dark)
          tertiary: "#a78bfa",      // Purple (lighter for dark)
          highlight: "rgba(96, 165, 250, 0.1)",
          textHighlight: "#b3aa0288",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.NotFoundPage(),
    ],
  },
}

export default config
