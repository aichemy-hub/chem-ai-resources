from pathlib import Path
import yaml


def define_env(env):
    """
    mkdocs-macros hook: load resources from YAML and expose helper functions.
    This is called once at build time.
    """
    data_path = Path("data") / "resources.yml"
    resources = yaml.safe_load(data_path.read_text())

    # Make the full list available as {{ resources }} in templates
    env.variables["resources"] = resources

    @env.macro
    def resources_by_domain(domain):
        """
        Return resources filtered by domain, e.g. 'foundations', 'chemistry', 'materials'.
        Usage in Markdown: {% for r in resources_by_domain("chemistry") %} ... {% endfor %}
        """
        return [r for r in resources if r.get("domain") == domain]
