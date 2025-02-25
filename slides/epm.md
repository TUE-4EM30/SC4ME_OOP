---
layout: two-cols
class: large-python-motion
---

## Encapsulation 

#### &nbsp;
### Attributes can be made private to hide and protect them.

<v-click>

- Python does this by adding two leading underscores to an attribute name.
</v-click>
<v-click>

- Allows the object developer to ensure conditions through `asserts`.
</v-click>

<v-click>

- Encapsulation allows object users to focus on what an object does, without
being concerned by how it is done.
- Although the programmer should be aware of the object's behavior (complexity).
</v-click>

<!-- Some languages do this by explicit type declarations (C++), others by naming convention -->
<!-- (Python). -->

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/classes_v2.py python 
<<< @/snippets/classes_v4_1.py python {3,9-11}
<<< @/snippets/classes_v4.py python {4,16-20}
````

---
layout: two-cols-header
---

## Why use encapsulation?

::left::

````md magic-move
<<< @/snippets/classes_v4.py python
<<< @/snippets/classes_v4.py python {11,12,16-19}
<<< @/snippets/classes_v4.py python {6,10,15}
````

::right::

- **Object refactoring ➡** Objects can be improved - both in terms of internal data structures and method implementations - without changing its interface.
<v-click at=1>

- **Code robustness ➡** The risk of unexpected behavior by unintended manipulation of data is minimized by shielding internal data.
</v-click>
<v-click  at=2>

- **Verification ➡** The object’s interface defines the functionality to be tested.
</v-click>

--- 
layout: two-cols
---

## Python *vs.* C++ | Encapsulation
#### &nbsp;
### Python *(naming convention)*

````md magic-move
<<< @/snippets/python_vs_c_pv2.py python
````

::right::

## &nbsp;
#### &nbsp;
### C++ *(public/private keywords)*

````md magic-move
<<< @/snippets/python_vs_c_cv2.c cpp 
````

---
layout: two-cols
class: large-python-motion
---

## Polymorphism
#### &nbsp;
### The behavior of a function or operator depends on the object it is applied to and/or its arguments (overloading)

- Argument-dependent implementation

<v-click>

- Magic methods define built-in methods and operators
    - Constructor: `__init__`
    - String representation: `__repr__`
    - Function call: `__call__`
    - Length function: `__len__`
</v-click>

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/classes_v10.py python {8-12}
<<< @/snippets/classes_v5.py python {5,6,8,9,18,19,21,22}
<<< @/snippets/classes_v6.py python
````

--- 
layout: two-cols
class: large-python-motion
---

## Python *vs.* C++ | Polymorphism
#### &nbsp;
### Python *(magic method)*

````md magic-move
<<< @/snippets/python_vs_c_pv3.py python
````

::right::

## &nbsp;
#### &nbsp;
### C++ *(method or external function)*

````md magic-move
<<< @/snippets/python_vs_c_cv3.c cpp
````