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
- Note that the provided code *does not yet implement mutations*.

::right::

<<<@/snippets/structure.txt {*}{lines:false}

---
layout: iframe
url: https://www.pygame.org/docs/_static/pygame_powered.svg
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

<<<@/snippets/main_v1.py py {9|11-12,16|13|14|15|18}{lines:false}

::right::

## &nbsp;

1. The simulation is initialized.

<v-click at=1>

2. With a fixed frame rate (`fps`), the simulation:
</v-click>

<v-click at=2>

- Checks events, such as keys being pressed.
</v-click>

<v-click at=3>

- Updates the state of the model (creature positions, graphs, *etc.*)
</v-click>

<v-click at=4>

- Displays the updated state.
</v-click>

<v-click at=5>

3. Terminates the simulation.
</v-click>