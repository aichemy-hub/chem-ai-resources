# All resources

Below is a small, growing collection of **free / open** resources at the
interface between chemistry, materials and machine learning / AI.

---

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain("foundations") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}

</div>

## Chemistry

<div class="grid cards" markdown>

{% for r in resources_by_domain("chemistry") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}

</div>

## Materials

<div class="grid cards" markdown>

{% for r in resources_by_domain("materials") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

{% endfor %}

</div>
