---
layout: two-cols
class: large-python-motion
---

## Data protection - Encapsulation 

Encapsulation is implemented by making attributes private, i.e., by hiding them. Some
languages do this by explicit type declarations (C++), others by naming conventions
(Python).

Encapsulation allows the program developer to focus on what an object does, without
being concerned by how it is done exactly.

::right::

&nbsp;

````md magic-move
<<< @/snippets/classes_v2.py python 
<<< @/snippets/classes_v4_1.py python {3,9-11}
<<< @/snippets/classes_v4.py python {4,16-20}
````

---
layout: two-cols
class: large-python-motion
---

## Data protection - Encapsulation 

Technical advantages:

<v-click>

- Object refactoring: Objects can be improved, both in terms of internal data structures and method implementations, without changing its interface.

</v-click>
<v-click>

- Code robustness: The risk of unexpected behavior by unintended manipulation of data is minimized by shielding internal data.

</v-click>
<v-click>

- Verification: The object’s interface defines the functionality to be tested.

</v-click>

::right::

&nbsp;

````md magic-move {at:2}
<<< @/snippets/classes_v4.py python {3,4,13,20}
<<< @/snippets/classes_v4.py python {11,12,16-19}
<<< @/snippets/classes_v4.py python {10,15}
````

--- 
layout: two-cols
class: large-python-motion
---

## Python vs C++ | Encapsulation

<br>

### Python

````md magic-move {at:1}
<<< @/snippets/python_vs_c_pv1.py python
<<< @/snippets/python_vs_c_pv2.py python
````

- Private by name convention: two leading underscores

::right::

&nbsp;

### C++

````md magic-move {at:1}
<<< @/snippets/python_vs_c_cv1.c c 
<<< @/snippets/python_vs_c_cv2.c c 
````

- Public/private by keyword

---
layout: two-cols
class: large-python-motion
---

## Operator overloading - Polymorphism

A function or operator can be applied to objects of different types. Its behavior depends on the type of argument(s).

Polymorphism is implemented by provision of special methods (so-called Magic Methods in Python )

````md magic-move {at:1}
<<< @/snippets/epm_v1.py python
<<< @/snippets/epm_v1.py python {6}
<<< @/snippets/epm_v1.py python {6}
<<< @/snippets/epm_v1.py python {6}
<<< @/snippets/epm_v1.py python {6}
````

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/DRY_v0.py python 
<<< @/snippets/classes_v2.py python
<<< @/snippets/classes_v2.py python {5,6,17,18}
<<< @/snippets/classes_v5.py python {5,6,8,9,18,19,21,22}
<<< @/snippets/classes_v6.py python
````

--- 
layout: two-cols
class: large-python-motion
---

## Python vs C++ | Polymorphism

<br>

### Python

````md magic-move {at:1}
<<< @/snippets/python_vs_c_pv2.py python
<<< @/snippets/python_vs_c_pv3.py python
````

- Operator as method

::right::

&nbsp;

### C++

````md magic-move {at:1}
<<< @/snippets/python_vs_c_cv2.c c
<<< @/snippets/python_vs_c_cv3.c c 
````

- Operator as method or external function


