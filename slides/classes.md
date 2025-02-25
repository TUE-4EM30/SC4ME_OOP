---
layout: two-cols
---

## Classes & Objects

#### &nbsp;
### A **class** defines the template from which an **object** (instance) is constructed.

<v-click>

- An object is created using the `__init__` magic method, know as the constructor.
</v-click>
<v-click>

- Attributes store data related to the object in `self`. They define the state of an object.
</v-click>
<v-click>

- Methods are functions in a class that define what an object can do. They normally take `self` as the first argument.
</v-click>
<v-click>

- Attributes and functions can be accessed through the instance.
</v-click>
<v-click>

- Objects can create complex data types with accompanying methods.
</v-click>

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/classes_v1.py python 
<<< @/snippets/classes_v1.py python {2}
<<< @/snippets/classes_v1.py python {2,3}
<<< @/snippets/classes_v1.py python {5,6}
<<< @/snippets/classes_v2.py python {8,9,14-18}
<<< @/snippets/classes_v3.py python {2-4,6-8,13,14,19,20}
````

--- 
layout: two-cols
---

## Python *vs.* C++
#### &nbsp;
### Python

<<< @/snippets/python_vs_c_pv1.py python

::right::

## &nbsp;
#### &nbsp;
### C++

<<< @/snippets/python_vs_c_cv1.c cpp