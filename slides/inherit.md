---
layout: two-cols
---

## The DRY princinple
#### &nbsp;
### **D**on't **R**epeat **Y**ourself:
- Avoid code duplication by making code reusable and modular.

<v-click>

- Compose objects such that repetition is avoided.
</v-click>
<v-click>

- Improves robustness and maintainability.
</v-click>
<v-click>

- More rigorous abstraction possible.
</v-click>

::right::

## &nbsp;

````md magic-move {at:1}
<<< @/snippets/DRY_v1.py python {11-12,23-24}
<<< @/snippets/DRY_v1b.py python
<<< @/snippets/DRY_v1c.py python {7-8}
<<< @/snippets/DRY_v1d.py python {11-12,23-24}
````

---
layout: two-cols
---

## Inheritance
#### &nbsp;
### Instead of repeating attributes and methods, a *child* class can inherit these from one or more *parents*.
- The *parent* `Shape` has the `color` attribute and `tell_color` method.

<v-click>

- The *child* `Circle` inherits these from its parent `Shape`.
</v-click>

<v-click>

- Less repetition, easier maintenance, improved modularity.
</v-click>

::right::

## &nbsp;

````md magic-move {at:1}
<<< @/snippets/DRY_v2.py python {3-8|10-12}
<<< @/snippets/DRY_v2b.py python
````

---

## Inheritance

#### &nbsp;

Inheritance is useful when:
- There exists an 'is a type of' relationship between objects.
- There is more than one child.
- Each child should expose the full parent (public) interface

<v-click>

### &nbsp;

### Composition over inheritance: favor object composition over class inheritance.
#### [Design Patterns: Elements of Reusable Object-Oriented Software]
</v-click>

---
layout: two-cols
class: large-python-motion
---

## Python *vs.* C++ | Inheritance
#### &nbsp;
### Python *(optional base class method)*
```python
class Polygon:
  def __init__(self, nverts):
    self.nverts = nverts

  def area(self):
    raise NotImplementedError

class Square(Polygon):
  def __init__( self, size ):
    self.__size = size
    Polygon.__init__( self, nverts=4 )

  def area( self ):
    return self.__size**2
```

::right::

&nbsp;

### C++ *(virtual enforces implementation)*

```cpp
class Polygon {
  public:
    Polygon(int _nverts){nverts=_nverts;}
    
    virtual float area();
    
    int nverts;
};

class Square : public Polygon{
  public:
    Square(int _size) : Polygon(4){size = _size}
    float area() {
      return size * size;
    }

  private:
    float size;
};
```