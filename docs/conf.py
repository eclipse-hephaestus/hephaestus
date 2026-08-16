# ********************************************************************************
# * Copyright (c) 2026 Contributors to the Eclipse Foundation
# *
# * See the NOTICE file(s) distributed with this work for additional
# * information regarding copyright ownership.
# *
# * This program and the accompanying materials are made available under the
# * terms of the Apache License 2.0 which is available at
# * https://www.apache.org/licenses/LICENSE-2.0
# *
# * SPDX-License-Identifier: Apache-2.0
# ********************************************************************************
import sys
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
REPO_ROOT = ROOT.parent

sys.path.insert(0, str(REPO_ROOT / "scripts"))
import hugo_intersphinx as hi

project = "Eclipse SDV Hephaestus Documentation"
copyright = "2026, Eclipse Foundation and contributors"
author = "Eclipse SDV Hephaestus"

extensions = [
    "myst_parser",
    "sphinx_needs",
    "sphinx.ext.intersphinx",
]

myst_enable_extensions = ["colon_fence"]

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- sphinx-needs (used under requirements/) ----------------------------------
needs_types = [
    dict(directive="req", title="Requirement", prefix="REQ_", color="#BFD8D2", style="node"),
    dict(directive="spec", title="Specification", prefix="SPEC_", color="#FEDCD2", style="node"),
    dict(directive="impl", title="Implementation", prefix="IMPL_", color="#DF744A", style="node"),
    dict(directive="test", title="Test Case", prefix="TEST_", color="#DCB239", style="node"),
]
needs_id_required = True
# Exported to <outdir>/needs.json — usable by external tooling, or by
# needs_external_needs if another sphinx-needs project is ever added.
needs_build_json = True
# needflow defaults to the "plantuml" engine (needs a Java + PlantUML
# toolchain we don't have); use graphviz instead, which is a plain `dot`
# binary and already required for the diagrams we build.
needs_flow_engine = "graphviz"

# -- intersphinx: link into the Hugo marketing site ---------------------------
intersphinx_mapping = {}
hi.add_hugo_intersphinx(intersphinx_mapping, REPO_ROOT)

# -- HTML output --------------------------------------------------------------
html_theme = "furo"
# The shared-nav header already shows the project name/logo; don't repeat it
# as plain text in Furo's own sidebar.
html_theme_options = {"sidebar_hide_name": True}

_shared_nav = hi.shared_nav_html_config(REPO_ROOT)
html_static_path = _shared_nav["html_static_path"]
html_css_files = _shared_nav["html_css_files"] + [
    "needs-dark-mode.css",
    "wide-screen-layout.css",
    "header-offset.css",
]
html_js_files = _shared_nav["html_js_files"]
if "html_extra_path" in _shared_nav:
    html_extra_path = _shared_nav["html_extra_path"]
