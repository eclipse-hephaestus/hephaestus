// Renders a header matching the Hugo site's own layouts/partials/site-header.html
// markup 1:1 (same classes, logo, nav links, CTA button), styled by the
// matching rules in shared-nav.css. Sourced from nav.json (generated from
// Hugo's index.json by scripts/hugo_json_to_objects_inv.py). Works from any
// page depth via Sphinx's DOCUMENTATION_OPTIONS.URL_ROOT. Fails silently if
// nav.json is missing (e.g. a standalone `sphinx-build` without the full
// pipeline).
(function () {
  "use strict";

  var urlRoot =
    (window.DOCUMENTATION_OPTIONS && window.DOCUMENTATION_OPTIONS.URL_ROOT) || "./";

  loadFont();

  fetch(urlRoot + "nav.json")
    .then(function (response) {
      return response.ok ? response.json() : null;
    })
    .then(function (data) {
      if (data) {
        renderHeader(data);
      }
    })
    .catch(function () {
      /* no nav.json available; skip the shared header */
    });

  function loadFont() {
    var link = document.createElement("link");
    link.rel = "stylesheet";
    link.href =
      "https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap";
    document.head.appendChild(link);
  }

  function renderHeader(data) {
    var site = data.site || {};

    // Mirrors layouts/partials/site-header.html:
    // <header class="site-header"><div class="container nav-wrap">...
    var header = document.createElement("header");
    header.className = "site-header";

    var wrap = document.createElement("div");
    wrap.className = "container nav-wrap";

    var brand = document.createElement("a");
    brand.className = "brand";
    brand.href = site.baseURL || "/";
    brand.setAttribute("aria-label", (site.title || "Eclipse SDV Hephaestus") + " home");
    if (site.logo) {
      var logo = document.createElement("img");
      logo.src = (site.baseURL || "/") + site.logo;
      logo.alt = (site.title || "Eclipse SDV Hephaestus") + " logo";
      brand.appendChild(logo);
    }
    var brandText = document.createElement("span");
    brandText.textContent = site.title || "Eclipse SDV Hephaestus";
    brand.appendChild(brandText);
    wrap.appendChild(brand);

    var links = document.createElement("nav");
    links.className = "main-nav";
    links.setAttribute("aria-label", "Main navigation");
    (data.nav || []).forEach(function (item) {
      var a = document.createElement("a");
      a.href = item.url;
      a.textContent = item.name;
      links.appendChild(a);
    });
    wrap.appendChild(links);

    if (site.callToActionText && site.callToActionURL) {
      var cta = document.createElement("a");
      cta.className = "btn btn-primary btn-small";
      cta.href = site.callToActionURL;
      cta.textContent = site.callToActionText;
      wrap.appendChild(cta);
    }

    header.appendChild(wrap);
    document.body.insertBefore(header, document.body.firstChild);
  }
})();
