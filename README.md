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
# Eclipse SDV Hephaestus website

A Hugo-based, GitHub Pages-ready website for the Eclipse SDV Hephaestus SDV tooling project built on the official Eclipse Foundation [`hugo-solstice-theme`](https://gitlab.eclipse.org/eclipsefdn/software-dev/frameworks-and-tools/hugo-solstice-theme).

## What is included

```text
.
├── .github/workflows/pages.yml      # GitHub Pages deployment workflow
├── archetypes/default.md            # Hugo content archetype
├── assets/scss/hephaestus.scss      # Placeholder for future SCSS pipeline
├── content/                         # Homepage and section pages
├── layouts/                         # Hugo templates and partials
├── static/css/hephaestus.css        # Project stylesheet
├── static/images/hephaestus/        # SVG logo and illustrations
├── themes/hugo-solstice-theme/      # Eclipse Solstice theme (git submodule)
├── hugo.toml                        # Hugo site configuration
└── README.md
```

## Local development

Install Hugo Extended, then clone the repository with submodules:

```bash
git clone --recurse-submodules https://github.com/eclipse-hephaestus/hephaestus.git
```

If you already cloned without `--recurse-submodules`, initialise the theme submodule first:

```bash
git submodule update --init --recursive
```

Then run:

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

## Theme

The site uses the official Eclipse Foundation `hugo-solstice-theme` pinned at tag `v3.0.1`, included as a git submodule at `themes/hugo-solstice-theme/`.

Hephaestus-specific overrides are kept under `layouts/partials/hephaestus/` and `static/css/hephaestus.css`.

To update the theme to a newer release:

```bash
cd themes/hugo-solstice-theme
git checkout <new-tag>
cd ../..
git add themes/hugo-solstice-theme
git commit -m "chore: update hugo-solstice-theme to <new-tag>"
```

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

Homepage sections are rendered from partials in `layouts/partials/hephaestus/`.

## Notes

- This repository intentionally avoids committing generated build output.
- The workflow uses the current GitHub Pages artifact deployment model.
- SVG assets are included so the first deployment works without external images.
