#!/usr/bin/env python3
"""Convert Hugo's public/index.json page inventory into a Sphinx-compatible
objects.inv, so sphinx-needs (or any Sphinx project) can intersphinx-link
into Hugo pages by section/kind via `:doc:`/`:ref:` roles. Also copies the
site/nav portion to nav.json for the shared top-nav bar (see
requirements/_static/shared-nav.js).

Usage:
    hugo_json_to_objects_inv.py <index.json> <objects.inv output> [<nav.json output>]

Must run after `hugo build` (which produces index.json) and before
`sphinx-build` for the requirements/ project (which reads the generated
inventory via intersphinx_mapping in requirements/conf.py, and serves
nav.json via html_extra_path).
"""
import json
import os
import sys

import sphobjinv as soi


def build_inventory(index_json_path: str, project: str, version: str) -> soi.Inventory:
    with open(index_json_path, encoding="utf-8") as f:
        data = json.load(f)

    inv = soi.Inventory()
    inv.project = project
    inv.version = version

    for page in data["pages"]:
        # `path` is relative to the site root, independent of Hugo's
        # baseURL subpath — stable across forks that use a different repo
        # name, unlike `relPermalink` which bakes that subpath in.
        name = page["path"].strip("/") or "index"
        inv.objects.append(
            soi.DataObjStr(
                name=name,
                domain="std",
                role="doc",
                priority="-1",
                uri=page["relPermalink"],
                dispname=page["title"] or name,
            )
        )

    return inv


def write_nav_json(index_json_path: str, nav_out_path: str) -> None:
    with open(index_json_path, encoding="utf-8") as f:
        data = json.load(f)
    os.makedirs(os.path.dirname(nav_out_path) or ".", exist_ok=True)
    with open(nav_out_path, "w", encoding="utf-8") as f:
        json.dump({"site": data["site"], "nav": data["nav"]}, f, indent=2)


def main() -> int:
    if len(sys.argv) not in (3, 4):
        print(__doc__)
        return 1

    index_json_path, output_path = sys.argv[1], sys.argv[2]
    inv = build_inventory(index_json_path, project="Eclipse SDV Hephaestus", version="")

    text = inv.data_file(contract=True)
    compressed = soi.compress(text)
    soi.writebytes(output_path, compressed)
    print(f"Wrote {len(inv.objects)} entries to {output_path}")

    if len(sys.argv) == 4:
        nav_out_path = sys.argv[3]
        write_nav_json(index_json_path, nav_out_path)
        print(f"Wrote nav data to {nav_out_path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
