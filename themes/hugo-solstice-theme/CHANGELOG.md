# eclipsefdn-hugo-solstice-theme

## 3.1.0

### Minor Changes

- 2e7f59d: [Params] Add support for an array of styles & scripts with ESM support in site config

## 3.0.1

### Patch Changes

- 611ee9c: Fix `seo_title_suffix` not having a fallback which caused strange
  output in title tags
- 4b531a5: Update eclipse.org menu's explore projects link
- e2a7ae1: Fix featured story popup not using the `publish_target` parameter

## 3.0.0

### Major Changes

- d95247d: Extract Neptune into its own package

### Minor Changes

- 297c5d9: [Menu] Add Bring Your Project menu item

## 2.0.0

### Major Changes

- a703b87: Extract Astro into its own package

## 1.0.1

### Patch Changes

- 730d2dc: [SEO] Add seo_title_suffix fallback
- 18b980e: [Featured Story Popup] Fix publish target not applying

## 1.0.0

### Major Changes

- 49f11b9: Extract Quicksilver into its own package

## 0.3.3

### Patch Changes

- aa2ec26: Upgrade eclipsefdn-solstice-assets to 0.2.8 to resolve bugs
- 40a389d: Update @eclipsefdn/solstice-components peer dependency version

## 0.3.2

### Patch Changes

- 969234d: Upgrade dependencies

## 0.3.1

### Patch Changes

- 6ab91c0: [Footer] Fix footer z-index

## 0.3.0

### Minor Changes

- b1c65af: [Featured Story Popup] Add featured story popup component
- d1e7e7c: Add @eclipsefdn/solstice-components as peer dependency

## 0.2.6

### Patch Changes

- c7937d9: Upgrade dependencies

## 0.2.5

### Patch Changes

- 3177e60: Upgrade eclipsefdn-solstice-assets to 0.2.4

## 0.2.4

### Minor Changes

- 2e97e7a: [Menu] Add opensourceglobalvoices.org link and make marketplace links external
- bd4c174: [Astro Menu] Support target and external icons
- 72574fe: [Menu] Update adoptium marketplace link

## 0.2.3

### Patch Changes

- b12ce69: Upgrade eclipsefdn-solstice-assets to 0.2.2

## 0.2.2

### Patch Changes

- 0250cd9: [Jumbotron] Fix jumbotron detection when headline is missing but custom_jumbotron exists
- 9f2ebcc: Fix menu items and footer links scrolling to top

## 0.2.1

### Minor Changes

- f4e550d: Target neptune CSS by default

### Patch Changes

- 4d3a118: Upgrade eclipsefdn-solstice-assets to 0.2.1
- d02c9fc: [Featured Footer] Fix publish target not applying

## 0.2.0

### Minor Changes

- 405c999: Add Neptune theme support

### Patch Changes

- 5cf19af: [Menu] Fix bad URLs from mass-domain edit

## 0.1.21

### Minor Changes

- 6c162aa: Update Twitter (X) icon
- af03914: [User Bios] Improve accessibility
- 1ea4b8b: [User Bios] Add flexible social links shortcode

## 0.1.20

### Minor Changes

- 1fe6e3f: Add site-wide format_title param

### Patch Changes

- 616bb60: [Agenda] Fix multiple streams not showing on mobile

## 0.1.19

### Patch Changes

- 312914d: Upgrade eclipsefdn-solstice-assets to 0.1.21

## 0.1.18

### Minor Changes

- 093b38a: Add default fallback for HubSpot forms

## 0.1.17

### Minor Changes

- db98f51: Update Quicksilver to support socials from params

## 0.1.16

### Minor Changes

- a25dd3d: Upgrade eclipsefdn-solstice-assets to 0.1.18
- 229ce92: Add option to hide or unformat seo_title and seo_title_suffix

## 0.1.15

### Patch Changes

- 0d3f05e: Upgrade eclipsefdn-solstice-assets to 0.1.17

## 0.1.14

### Minor Changes

- be6ddc4: Update social media links

## 0.1.13

### Minor Changes

- 2d4d4f3: Add Sponsor Directory to the menu

### Patch Changes

- 66af07f: Fix missing professional services link

## 0.1.12

### Minor Changes

- 7c47f0a: Add paginated video list shortcode
- 5db66a1: Add HTML shortcode

## 0.1.11

### Minor Changes

- 3a9f0cf: Add dateFormat params for news and events shortcode
- 6a18938: Upgrade hugo-solstice-theme and dependencies

### Patch Changes

- cfe1fa0: Prevent summaries from rendering HTML

## 0.1.10

### Minor Changes

- f3275be: Add body_class param
- 86d4bdd: Remove corporate sponsors page from menu

## 0.1.9

### Minor Changes

- 8a23f01: Upgrade theme to Hugo 0.144.2 and Node 22 LTS

## 0.1.8

### Minor Changes

- 7df36f1: Upgrade eclipsefdn-solstice-assets to 0.1.10

## 0.1.7

### Minor Changes

- fbaab3e: Add Bluesky social media support

### Patch Changes

- c64cfa0: Upgrade eclipsefdn-solstice-assets

## 0.1.6

### Minor Changes

- 1cabcee: Add flexible social media footer links
- 5b19cd3: Add ability to add IDs to jumbotron links and navbar CTA

## 0.1.5

### Minor Changes

- e2da793: Update newsletter form with new values

## 0.1.4

### Patch Changes

- bd541ba: Upgrade eclipsefdn-solstice-assets to 0.1.7
- 49f1f23: Fix news pagination not appearing

## 0.1.3

### Minor Changes

- 17be4c3: Upgrade social media icons to Font Awesome 6

## 0.1.2

### Patch Changes

- 505f118: Upgrade eclipsefdn-solstice-assets to 0.1.4

## 0.1.1

### Minor Changes

- 36a16d9: Add Instagram icon

### Patch Changes

- fee305e: Hide categories and remove duplicate search
- 7eb8859: [Agenda] Fix modal not listing multiple presenters

## 0.1.0

This is the first documented release in the changelog, but the project was in
development for some time before this release. For a full list of changes,
please see the commit history.

### Minor Changes

- 23f473e: Add style override CSS to head.html
- f47ad1c: Add property in jumbotron links param to override individual button classes
- d41f5fa: Add custom title support for related links partial
- 929aef1: Add working group footer
- b9365f1: Add id param to newsroom resources shortcode
- 0b9dc12: Add menu types support
- ae7d31a: Add support for custom deprecation message
- 1362bba: Add custom sidebar support

### Patch Changes

- c4de369: Fix mobile menu not supporting direct link menu items or basic dropdowns
- 5c82d70: Fix missing trailing slash to menu URLs
- 16d2020: Fix fragments dropped from sidebar links
