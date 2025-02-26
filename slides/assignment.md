---
layout: iframe
url: https://www.youtube.com/embed/0ZGbIKd0XrM
---

<!-- Primer video included from YouTube -->

---
layout: iframe
url: https://youtube.com/embed/gv80GPpk980
---

<!-- Video to own implementation -->

---
layout: two-cols
---

## TUEvolution 

- Simulation for the behavior and evolution of creatures in a virtual world.
- Models a population of creatures that interact with their environment and each other.
- Creatures can move, reproduce, and perish based on various factors such as food availability. 
- Observe how different traits and behaviors evolve over time in response to the environment.

::right::

<<<@/snippets/structure.txt {*}{lines:false}

---
layout: iframe
url: https://www.pygame.org
---

<!-- Link to pygame -->

---
layout: two-cols
---

## The `main.py` file

#### &nbsp;
- Starts the simulation when run as a script.
- Loads a scenario file (`default.toml`).
<<<@/snippets/default.toml toml {*}{lines:false,at:1}

<v-click>

- Instantiates the `App` object
</v-click>
<v-click>

- Executes the `App`
</v-click>

::right::

````md magic-move {at:1}
<<<@/snippets/main_v0.py py {4-12|14-21|23-24}{lines:false}
````

---
layout: two-cols
---

## The `execute` loop

::right::

## &nbsp;

````md magic-move {at:1}
<<<@/snippets/main_v1.py py {*}{lines:false}
````