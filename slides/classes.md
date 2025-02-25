---
layout: two-cols
class: large-python-motion
---

## Classes & objects

A class defines the template based on which an object (or instance) is constructed.

<br>

<v-click>

- Attributes are variables that store data related to the object. They define the state of an object.

</v-click>
<v-click>

- Methods are functions inside a class that define what an object can do.

</v-click>

<br>

<v-click>

- The initial Attibutes can also be altered in the main code.

</v-click>
<v-click>

- The Class can be expended to contain all information needed.

</v-click>

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/classes_v1.py python 
<<< @/snippets/classes_v1.py python {2,3}
<<< @/snippets/classes_v1.py python {5,6}
<<< @/snippets/classes_v2.py python {8,9,14-18}
<<< @/snippets/classes_v3.py python {2-4,6-8,13,14,19,20}
````

---
layout: two-cols
class: large-python-motion
---

## Classes & objects



<v-click>

Delegation: Passing tasks to another class

</v-click>
<v-click>

Composition: Using an object as part of another object

</v-click>
<v-click>

Extension: Creating new behavior by subclassing

</v-click>

::right::

&nbsp;

````md magic-move {at:1}
<<< @/snippets/DRY_v0.py python
<<< @/snippets/classes_v7.py python
<<< @/snippets/classes_v8.py python 
<<< @/snippets/classes_v9.py python 
````