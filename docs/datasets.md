# Datasets and Dataset Collections

Below is a collection of **free / open** datasets and lists of datasets at the interface between chemistry, materials and machine learning / AI.

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("foundations", "dataset") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("chemistry", "dataset") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>

## Materials

<div class="grid cards" markdown>
{% for r in resources_by_domain_and_type("materials", "dataset") %}
- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>  
