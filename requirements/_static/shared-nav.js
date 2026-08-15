// Renders the same top navigation bar as the Hugo site's .site-header,
// sourced from nav.json (generated from Hugo's index.json by
// scripts/hugo_json_to_objects_inv.py). Works from any page depth via
// Sphinx's DOCUMENTATION_OPTIONS.URL_ROOT. Fails silently if nav.json is
// missing (e.g. a standalone `sphinx-build` without the full pipeline).
(function () {
  "use strict";

  var urlRoot =
    (window.DOCUMENTATION_OPTIONS && window.DOCUMENTATION_OPTIONS.URL_ROOT) || "./";

  fetch(urlRoot + "nav.json")
    .then(function (response) {
      return response.ok ? response.json() : null;
    })
    .then(function (data) {
      if (data) {
        renderNav(data);
      }
    })
    .catch(function () {
      /* no nav.json available; skip the shared bar */
    });

  function renderNav(data) {
    var bar = document.createElement("div");
    bar.className = "hephaestus-shared-nav";

    var inner = document.createElement("div");
    inner.className = "hephaestus-shared-nav__inner";

    var brand = document.createElement("a");
    brand.className = "hephaestus-shared-nav__brand";
    brand.href = (data.site && data.site.baseURL) || "/";
    brand.textContent = (data.site && data.site.title) || "Eclipse SDV Hephaestus";
    inner.appendChild(brand);

    var links = document.createElement("nav");
    links.className = "hephaestus-shared-nav__links";
    (data.nav || []).forEach(function (item) {
      var a = document.createElement("a");
      a.href = item.url;
      a.textContent = item.name;
      links.appendChild(a);
    });
    inner.appendChild(links);

    bar.appendChild(inner);
    document.body.insertBefore(bar, document.body.firstChild);
  }
})();
