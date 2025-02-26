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
- Study the general structure of the code
- Change `main.py` to:
    - Process new scenario file
    - Instantiate creatures accordingly
- Change `creatures.py` to:
    - Implement mutations

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
### Add a histogram plot for both the size distribution and the speed distribution, which updates every 'generation' and is available through the graph cycler.

::left::
<!-- misschien een toevoegen met de gevraagde historgram? -->
<div class="flex justify-center">
  <img src="/images/graphcycler.png" alt="graphcycler" >
</div>

::right::

- Just included size and speed distributions
- Desire to visualize those distributions over the generations

---
layout: two-cols
---

## Question 2 (cont'd)

- Approach:
    - Create the histograms
    - Include the histograms into the graph cycler

<br>

<v-click at=2>

- Requirements:
    - The histograms should be updated every "generation" and be available through the graph cycler.
    - The histograms should work for both `deafult.toml` and `question1.toml`.
    - All previously stated requirements should still hold.

</v-click>

::right::

<<<@/snippets/main_v4.py {*}{lines:false}

---
layout: two-cols
---

## Question 2 (cont'd)
#### &nbsp;
Tips:
- Study the general structure of the code
- Change `graphs.py` to:
    - Create a histogram `class`
- Change `main.py` to:
    - Include the histograms into the graph cycler

::right::

````md magic-move
<<<@/snippets/structure.txt {*|8,11}{lines:false}
<<<@/snippets/graphs_v1.py {*}{lines:false}
<<<@/snippets/graphs_v2.py {*}{lines:false}
<<<@/snippets/main_v4.py {*}{lines:false}
````

---
layout: two-cols-header
---

## Question 3
#### &nbsp;
### Implement a "sense" trait for the creature.

::left::

 - Based on the youtube video on the slides. Implement a "sense" trait for the creature. 
 - Explain the reasoning behind your implementation.
 - Design a `question3.toml` scenario that shows an interesting simulation to demonstrate this trait. 
 - Make sure the "sense" circle is visualized in the simulation. 

 
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
    - Implement the "sense" trait.
    - Vizualize the "sense" trait.
    - Tweek the parameters and design a 'question3.tolm` scenario that shows an interesting simulation to demonstrate this trait.
    
<v-click at=2>

- Requirements:
    - Like the size and speed traits, the sense treat should also be configurable through the `toml` file.
    - All previously stated requirements should still hold.
</v-click>

::right::


---

## Submission instructions

- Rubric
- Report
- Gitlab


<!-- Current code does not consider mutations. -->