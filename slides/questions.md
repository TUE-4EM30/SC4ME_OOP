---
layout: two-cols-header
---

## Question 1
#### &nbsp;
### Extent the code with size and speed mutations, such that the `question1.toml` scenario can be simulated.

::left::

<<<@/snippets/question1.toml toml {*}{lines:false}

::right::

- When a creature reproduces, there is a chance for mutations to take place.
- The size and speed of a child relative to that of its parent will:
    - Stay the same with probability $\frac{1}{2}$
    - Increase by 1 with probability $\frac{1}{4}$
    - Decrease by 1 with probability $\frac{1}{4}$
- The size and speed are independent random variables.
- Larger creatures will eat smaller creatures.

---
layout: two-cols
---

## Question 1 (cont'd)

- Approach:
    - Change the `scenario` in the `main.py` file to `question1`.
    - Modify the code to attain the required behavior.

<br>

<v-click at=2>

- Requirements:
    - The `default.toml` and `question1.toml` files may not be changed.
    - The modified code must still run - and give the same results - for the `default.toml`.
    - The different scenarios should be runable by changing the `scenario` in `main.py` only.
</v-click>

::right::

````md magic-move {at:1}
<<<@/snippets/main_v0.py py {7}{lines:false}
<<<@/snippets/main_v2.py py {7}{lines:false}
<<<@/snippets/main_v2.py py {*}{lines:false}
````

---
layout: two-cols
---

## Question 1 (cont'd)
#### &nbsp;
Tips:
- Study the general structure of the code.

<v-click at=2>

- Change `main.py` to:
    - Process new scenario file.
    - Instantiate creatures accordingly.
</v-click>

<v-click at=3>

- Change `creatures.py` to:
    - Implement the size and speed mutations.
    - Use the `numpy.random` module.
</v-click>

::right::

````md magic-move
<<<@/snippets/structure.txt {*|8,10}{lines:false}
<<<@/snippets/main_v3.py py {*}{lines:false}
<<<@/snippets/creatures_v1.py py {*}{lines:false}
````

---
layout: two-cols-header
---

## Question 2
#### &nbsp;
### Add two histogram plots showing the size and speed distributions.

::left::
<!-- misschien een toevoegen met de gevraagde historgram? -->
<div class="flex justify-center">
  <img src="/images/histogram.png" alt="histogram" >
</div>

::right::

- When mutations take place, one wants to inspect how these are distributed and how these distributions change over the generations.
- Histograms can be used to visualize these distributions.

---
layout: two-cols
---

## Question 2 (cont'd)

- Approach & tips:
  - Study the `XY` class in `graphs.py` for inspiration.
  - Develop a `Histogram` class which has the required functionality.
  - Include the histograms in the graph cycler.

<v-click at=2>

- Requirements:
    - The histograms should be updated every generation.
    - The histograms should be available through the graph cycler.
    - The histograms should work properly for both `default.toml` and `question1.toml`.
    - All previously stated requirements should be met.
</v-click>

::right::

````md magic-move {at:1}
<<<@/snippets/graphs_v1.py {*}{lines:false}
<<<@/snippets/graphs_v2.py {*}{lines:false}
<<<@/snippets/main_v4.py {*}{lines:false}
````

---
layout: two-cols-header
---

## Question 3
#### &nbsp;
### Implement a *sense* trait for the creature.

::left::

- A creature can sense its surrounding in a (mutating) radius.
- The creature responds to the sense:
    - Goes directly to food.
    - Runs away from too large creatures (predators).
- The energy required to sense scales with the sensing radius.

::right::

<!-- misschien een toevoegen met de circles on the creatures heen? -->
<div class="flex justify-center">
  <img src="/images/sense.png" alt="sense" >
</div>

---
layout: two-cols
---

## Question 3 (cont'd)

- Approach:
    - Implement the sense trait.
    - Visualize the sense radius per creature in the simulation.
    - Design a `question3.tolm` scenario that demonstrate the sense trait.
    - Explain the reasoning behind your implementation in the report.

::right::

## &nbsp;

- Requirements:
    - Like the size and speed traits, the sense trait should be configurable through the `toml` scenario file.
    - The `default.toml` and `question1.toml` scripts should not be altered and should continue to run.
    - All previously stated requirements still hold.

---

## Submission instructions

- The following deliverables are due on **Friday March 21, 2025, 18:00**:
    - All **source code** must be developed in your team’s Gitlab repository. After the due date a snapshot of your repository will be taken. The latest push to the Gitlab repository main branch before the deadline will be assessed.
    - Provide a short report discussing the reasoning behind your solutions to the questions. Include relevant code snippets and screenshots if needed. Indicate your names, student numbers, and team number on the report. The report must be uploaded on Canvas (in pdf-file format) no later than the due date.
- Carefully read the Canvas rubric that accompanies the assignment.