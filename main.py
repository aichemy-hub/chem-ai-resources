from pathlib import Path
import yaml
from datetime import datetime, timezone

# Order in which domains should appear
DOMAIN_ORDER = ["foundations", "chemistry", "materials"]


def define_env(env):
    """
    mkdocs-macros hook: load resources from YAML and expose helper functions.
    This is called once at build time.
    """
    data_path = Path("data") / "resources.yml"
    resources = yaml.safe_load(data_path.read_text())

    # Make the full list available as {{ resources }} in templates
    env.variables["resources"] = resources
    env.variables["DOMAIN_ORDER"] = DOMAIN_ORDER

    @env.macro
    def resources_by_domain(domain):
        """
        Return resources filtered by domain, e.g. 'foundations', 'chemistry', 'materials'.
        Usage in Markdown: {% for r in resources_by_domain("chemistry") %} ... {% endfor %}
        """
        return [r for r in resources if r.get("domain") == domain]

    @env.macro
    def resources_by_domain_and_type(domain, res_type):
        """
        Return resources filtered by domain and type, e.g. 'chemistry' and 'Python package'.
        Usage in Markdown: {% for r in resources_by_domain_and_type("chemistry", "Python package") %} ... {% endfor %}
        """
        return [
            r
            for r in resources
            if r.get("domain") == domain and r.get("type") == res_type
        ]

    @env.macro
    def all_resources_sorted():
        """
        Return all resources sorted by DOMAIN_ORDER, then title.
        Usage in Markdown: {% for r in all_resources_sorted() %} ... {% endfor %}
        """

        def sort_key(r):
            domain = (r.get("domain") or "").lower()
            try:
                domain_index = DOMAIN_ORDER.index(domain)
            except ValueError:
                domain_index = len(DOMAIN_ORDER)
            return (domain_index, (r.get("title") or "").lower())

        return sorted(resources, key=sort_key)

    @env.macro
    def last_updated():
        return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
