---
layout: default
title: Reparto
permalink: /reparto/
---
<ul>
  {% for personaje in site.reparto %}
    <li>
      <a href="{{ personaje.url }}">{{ personaje.name }}</a><br/>
      {{ personaje.title }} — interpretada por {{ personaje.actor }}<br/>
      “{{ personaje.frase }}”
    </li>
  {% endfor %}
</ul>
