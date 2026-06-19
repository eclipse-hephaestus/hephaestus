<!--
 ********************************************************************************
 * Copyright (c) 2026 Contributors to the Eclipse Foundation
 *
 * See the NOTICE file(s) distributed with this work for additional
 * information regarding copyright ownership.
 *
 * This program and the accompanying materials are made available under the
 * terms of the Apache License 2.0 which is available at
 * https://www.apache.org/licenses/LICENSE-2.0
 *
 * SPDX-License-Identifier: Apache-2.0
 ********************************************************************************
-->
# Eclipse Hepheistos website

A Hugo-based, GitHub Pages-ready website starter for the Eclipse Hepheistos SDV tooling project.

The design is intentionally Solstice-aligned: Eclipse-style navigation, dark project hero, project CTAs, card grids, documentation pages, community links, and a minimal override layer that can later be wired to the official Eclipse `hugo-solstice-theme`.

## What is included

```text
.
â”œâ”€â”€ .github/workflows/pages.yml      # GitHub Pages deployment workflow
â”œâ”€â”€ archetypes/default.md            # Hugo content archetype
â”œâ”€â”€ assets/scss/hepheistos.scss      # Placeholder for future SCSS pipeline
â”œâ”€â”€ content/                         # Homepage and section pages
â”œâ”€â”€ layouts/                         # Hugo templates and partials
â”œâ”€â”€ static/css/hepheistos.css        # Project stylesheet
â”œâ”€â”€ static/images/hepheistos/        # SVG logo and illustrations
â”œâ”€â”€ hugo.toml                        # Hugo site configuration
â””â”€â”€ README.md
```

## Local development

Install Hugo Extended, then run:

```bash
hugo server -D
```

Open the local URL printed by Hugo.

## Build locally

```bash
hugo --gc --minify
```

The generated site is written to `public/`. Do not commit `public/`; GitHub Actions builds it for deployment.

## Deploy to GitHub Pages

1. Create a new GitHub repository.
2. Copy this folder into the repository root.
3. Commit and push to the `main` branch.
4. In GitHub, go to **Settings > Pages**.
5. Set **Source** to **GitHub Actions**.
6. Push a commit or run the workflow manually from the **Actions** tab.

The workflow in `.github/workflows/pages.yml` builds the Hugo site and publishes the generated `public/` folder using GitHub Pages artifacts.

## Configure the production URL

For a project site, change `baseURL` in `hugo.toml`:

```toml
baseURL = "https://YOUR-ORG.github.io/YOUR-REPOSITORY/"
```

For a user or organization site, use:

```toml
baseURL = "https://YOUR-ORG.github.io/"
```

The workflow also passes GitHub Pages' detected base URL at build time, so Pages deployments should still work after repository setup.

## Optional: wire to the official Eclipse Solstice theme

This starter is self-contained so it can be uploaded to GitHub and deployed immediately. To move closer to the official Eclipse Foundation web stack later, add the Solstice theme as a submodule and migrate only the base template/header/footer overrides that you want to keep:

```bash
git submodule add https://gitlab.eclipse.org/eclipsefdn/software-dev/frameworks-and-tools/hugo-solstice-theme.git themes/hugo-solstice-theme
```

Then set this in `hugo.toml`:

```toml
theme = "hugo-solstice-theme"
```

Keep the Hepheistos-specific partials under `layouts/partials/hepheistos/` and the project CSS under `static/css/hepheistos.css` or move it into the Solstice asset pipeline as needed.

## Editing content

Main pages live under `content/`:

- `content/_index.md` for the homepage metadata
- `content/getting-started/_index.md`
- `content/tooling/_index.md`
- `content/docs/_index.md`
- `content/community/_index.md`
- `content/downloads/_index.md`
- `content/news/_index.md`
- `content/faq/_index.md`

Homepage sections are rendered from partials in `layouts/partials/hepheistos/`.

## Notes

- This repository intentionally avoids committing generated build output.
- The workflow uses the current GitHub Pages artifact deployment model.
- SVG assets are included so the first deployment works without external images.
