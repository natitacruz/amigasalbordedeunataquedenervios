---
layout: creditos
title: Creditos
permalink: /creditos/
---

<div class="credits-wrapper">
  <div class="credits">
    {% for personaje in site.reparto %}
      <div class="credit-line">
        <a class="personaje-link" href="{{ site.baseurl }}{{ personaje.url }}">
          <strong>{{ personaje.actor }}</strong> como <span>{{ personaje.name }}</span><br/>
          <em>{{ personaje.title }}</em>
        </a>
      </div>
    {% endfor %}
  </div>
</div>
