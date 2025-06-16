---
layout: default
title: Reparto
permalink: /reparto/
---

<ul>
  {% for personaje in site.reparto %}
    <li>
      <a href="https://natitacruz.github.io/amigasalbordedeunataquedenervios{{ personaje.url }}">{{ personaje.name }}</a><br/>
      {{ personaje.title }} — interpretada por {{ personaje.actor }}<br/>
      “{{ personaje.frase }}”
    </li>
  {% endfor %}
</ul>
