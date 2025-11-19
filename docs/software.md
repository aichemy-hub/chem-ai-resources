# Software Resources

Below is a collection of **free / open** software resources at the interface between chemistry, materials and machine learning / AI.

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("foundations", "software") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("chemistry", "software") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>

## Materials

<div class="grid cards" markdown>
{% for r in resources_by_domain_and_type("materials", "software") %}
- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  

{% endfor %}
</div>  
