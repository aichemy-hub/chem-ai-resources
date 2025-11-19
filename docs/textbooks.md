# Online Textbooks

Below is a collection of **free / open** online textbooks at the interface between chemistry, materials and machine learning / AI.

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("foundations", "online textbook") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}
</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain_and_type("chemistry", "online textbook") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}
</div>

## Materials

<div class="grid cards" markdown>
{% for r in resources_by_domain_and_type("materials", "online textbook") %}
- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}
</div>  
