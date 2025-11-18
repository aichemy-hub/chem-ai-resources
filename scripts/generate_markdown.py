#!/usr/bin/env python3
import pathlib
import yaml  # pip install pyyaml

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "resources.yml"
OUT_PATH = ROOT / "resources.md"

DOMAIN_ORDER = ["foundations", "chemistry", "materials"]


def load_resources():
    with DATA_PATH.open() as f:
        resources = yaml.safe_load(f)
    # normalize domains & sort a bit
    for r in resources:
        r["domain"] = r.get("domain", "").lower()
    resources.sort(key=lambda r: (r["domain"], r["title"].lower()))
    return resources


def render_table(resources_for_domain):
    headers = [
        "Name",
        "Description",
        "Type",
        "Difficulty",
        "Prior knowledge",
        "Time",
    ]

    lines = []
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("| " + " | ".join(["---"] * len(headers)) + " |")

    for r in resources_for_domain:
        name = f"[{r['title']}]({r['url']})"
        desc = r.get("description", "").replace("\n", " ")
        # keep descriptions from exploding the table
        if len(desc) > 160:
            desc = desc[:157] + "..."
        row = [
            name,
            desc,
            r.get("type", ""),
            r.get("difficulty", ""),
            r.get("prior_knowledge", ""),
            r.get("est_time", ""),
        ]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def main():
    resources = load_resources()

    # Group by domain
    by_domain = {}
    for r in resources:
        by_domain.setdefault(r["domain"], []).append(r)

    md_parts = [
        "# Chemistry & Materials Machine Learning Resources",
        "",
        "_All resources are free / open access / open source as far as we are aware._",
        "",
        "Jump to:",
    ]

    for d in DOMAIN_ORDER:
        if d in by_domain:
            anchor = d.replace(" ", "-")
            md_parts.append(f"- [{d.title()}](#{anchor})")
    md_parts.append("")

    for d in DOMAIN_ORDER:
        if d not in by_domain:
            continue
        anchor = d.replace(" ", "-")
        md_parts.append(f"## {d.title()}")
        md_parts.append("")
        md_parts.append(render_table(by_domain[d]))
        md_parts.append("")

    OUT_PATH.write_text("\n".join(md_parts))
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
