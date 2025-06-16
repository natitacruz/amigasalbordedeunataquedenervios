---
layout: creditos
title: Creditos
permalink: /creditos/
---

<div class="credits-columns">
  <div class="credits-column">
    {% assign mitad = site.reparto | size | divided_by: 2 %}
    {% for personaje in site.reparto limit: mitad %}
      <div class="credit-line">
        <a class="personaje-link" href="{{ site.baseurl }}{{ personaje.url }}">
          <strong>{{ personaje.actor }}</strong> como <span>{{ personaje.name }}</span><br/>
          <em>{{ personaje.title }}</em>
        </a>
      </div>
    {% endfor %}
  </div>

  <div class="credits-column">
    {% assign mitad = site.reparto | size | divided_by: 2 %}
    {% for personaje in site.reparto offset: mitad %}
      <div class="credit-line">
        <a class="personaje-link" href="{{ site.baseurl }}{{ personaje.url }}">
          <strong>{{ personaje.actor }}</strong> como <span>{{ personaje.name }}</span><br/>
          <em>{{ personaje.title }}</em>
        </a>
      </div>
    {% endfor %}
  </div>
</div>
