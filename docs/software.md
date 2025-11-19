# Software Resources

Below is a collection of **free / open** software resources at the interface between chemistry, materials and machine learning / AI.

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("foundations", "software") %}

- **[{{ r.title }}]({{ r.url }})**  

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}
    **License:** {{ r.license }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}
</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("chemistry", "software") %}

- **[{{ r.title }}]({{ r.url }})**  

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}
    **License:** {{ r.license }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}
</div>

## Materials

<div class="grid cards" markdown>
{% for r in resources_by_domain_and_type("materials", "software") %}

- **[{{ r.title }}]({{ r.url }})**  

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}
    **License:** {{ r.license }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}
</div>  
