# Quick links

A compact, at-a-glance index of all resources in this site.

Use this when you just want a link and rough idea of what it is, without the
full description.

| Name | Domain | Type | Difficulty | Time |
| --- | --- | --- | --- | --- |
{% for r in all_resources_sorted() -%}
| [{{ r.title }}]({{ r.url }}) | {{ r.domain|title }} | {{ r.type }} | {{ r.difficulty|title }} | {{ r.est_time }} |
{% endfor %}
