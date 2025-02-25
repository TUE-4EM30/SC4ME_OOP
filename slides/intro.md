---
layout: two-cols-header
---

## Previously...

## &nbsp;

### OOP is a programming paradigm based on *objects*, which are *abstract data structures* containing:
- Data (attributes or member variables)
- Procedures acting on the data (methods or member functions)

::left::

```python {1-4|6-14}{lines: false}
In [1]: my_list = ['One', 'Two', 'Three']

In [2]: type(my_list)
Out[2]: list

In [3]: dir(my_list)
Out[3]: 
['__add__',
    ⋮
 'append',
    ⋮
 'index',
 'insert',
    ⋮
 'sort']
```

::right::

- `my_list` is an object (instance) of type (class) `list`
- Data is stored internally in `my_list`

<v-click at=1>

- `list` implements lots of methods
- Python offers lots of other [built-in types](https://docs.python.org/3/library/stdtypes.html), including: `int`, `float`, `complex`, `str`, `bool`, `tuple`, `range`, `dict`
</v-click>

---
layout: two-cols
---

## Previously...

<<< @/snippets/studentGitlabStatus.py {*}{lines:true}

::right::

## &nbsp;

- Built-in types and *module* imports provide a wealth of possibilities

<v-click>

- Creating *classes* and *objects* can be useful for:
    - Bundling and protecting complex data types
    - Repetitive use of complex data types
    - Defining methods specific to complex data types
    - Separating functionality and implementation
    - Modeling real entities
</v-click>