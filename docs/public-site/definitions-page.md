# Public Definitions Page

[`definitions/index.html`](../../definitions/index.html) — the official Matrix Definitions design
(from `agent-matrix/design` → `scout/Matrix-Definitions.html`), implemented faithfully as a single
premium GitHub Pages page served at `/definitions` (proxied as `https://ruslanmv.com/definitions`).

Self-contained (inline CSS/JS, one fonts link): two-column hero with an animated particle-mesh
pack card, trust row, "what this repository defines" panel, ecosystem row, quality profiles,
two-column "verify the current pack" block, and footer. Scroll-reveal, copy-to-clipboard, nav
active-on-scroll. The current-pack version is read live from `packs/current/manifest.json`
(fallback `../VERSION`, then `2026.06.0`). Repo/GitHub links point at `agent-matrix/matrix-definitions`.

Preview: `python -m http.server 8080` → http://localhost:8080/definitions/
