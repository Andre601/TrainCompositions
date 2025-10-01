# Train Compositions

This site lists all the known Train Compositions (locomotives, passenger carts, etc.) that currently travel for specific lines on the Community Server of MrJulsen.

## Legend

<span class="carriage locomotive">T</span> = Locomotive  
<span class="carriage">1</span> = 1st class  
<span class="carriage">2</span> = 2nd class  
<span class="carriage">1/2</span> = 1st and 2nd class  
<span class="carriage">R</span> = Restaurant

## Trains

{% set json = load_json("docs/assets/trains.json") %}

{% for line, trains in json.items() %}
### {{ line }}

{% for provider, composition in trains.items() %}
**Provider:** {{ provider }}

{% for part in composition -%}
<span class="carriage {% if part == 't' %}locomotive{% endif %}" title="{{ set_title(part) }}">{{ part | upper() }}</span>
{%- endfor %}
{% endfor %}
{% endfor %}