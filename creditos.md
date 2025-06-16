---
layout: creditos
title: Creditos
permalink: /creditos/
---

<div class="credits-column">
  {% for personaje in site.reparto limit: site.reparto.size | divided_by: 2 %}
    <div class="credit-line">
      <a class="personaje-link" href="{{ site.baseurl }}{{ personaje.url }}">
        <strong>{{ personaje.actor }}</strong> como <span>{{ personaje.name }}</span><br/>
        <em>{{ personaje.title }}</em>
      </a>
    </div>
  {% endfor %}
</div>

<div class="credits-column">
  {% for personaje in site.reparto offset: site.reparto.size | divided_by: 2 %}
    <div class="credit-line">
      <a class="personaje-link" href="{{ site.baseurl }}{{ personaje.url }}">
        <strong>{{ personaje.actor }}</strong> como <span>{{ personaje.name }}</span><br/>
        <em>{{ personaje.title }}</em>
      </a>
    </div>
  {% endfor %}
</div>
