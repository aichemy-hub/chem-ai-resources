# All resources

## Foundations

<div class="grid cards" markdown>

{% for r in resources_by_domain("foundations") %}

- **[{{ r.title }}]({{ r.url }})**  
    _{{ r.type|capitalize }} · {{ r.difficulty|title }}_

    {{ r.description }}

    **Prior knowledge:** {{ r.prior_knowledge }}  
    **Estimated time:** {{ r.est_time }}

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

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

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

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

    {% for tag in r.tags %}<span class="tag-pill">{{ tag }}</span>{% endfor %}

{% endfor %}

</div>
