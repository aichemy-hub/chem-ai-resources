# Datasets and Dataset Collections

Below is a collection of **free / open** datasets and lists of datasets
at the interface between chemistry, materials and machine learning / AI.

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain("foundations") if r.type == "dataset" %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}

</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain("chemistry") if r.type == "dataset" %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}

</div>

## Materials

<div class="grid cards" markdown>

{% for r in resources_by_domain("materials") if r.type == "dataset" %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}

</div>
