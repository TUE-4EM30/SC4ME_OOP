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

---
layout: two-cols
---

## Question 1 (cont'd)

- Approach:
    - Change the `scenario` in the `main.py` file to `question1`.
    - Modify the code to attain the required behavior.


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
````

---

## Submission instructions

- Rubric
- Report
- Gitlab


<!-- Current code does not consider mutations. -->