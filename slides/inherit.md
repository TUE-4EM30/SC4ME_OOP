
---
layout: two-cols
---

## Classes & Objects



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

---
layout: two-cols
class: large-python-motion
---

## Don't Repeat Yourself (DRY)

The "Do Not Repeat Yourself" (DRY) principle means avoiding code duplication by making code reusable and modular. This improves maintainability and reduces errors.

<v-click>

If separate classes for Circles and Rectangles
- Duplicate code: The color attribute and describe() method are repeated.
- Harder maintanance: If we want to add a border_color, we must update every class separately.

</v-click>

::right::

&nbsp;

<v-click at="1">

<<< @/snippets/DRY_v1.py python

</v-click>

---
layout: two-cols
class: large-python-motion
---

## Inheritance

Instead of repeating attributes and methods, we move common code into a parent class (Shape) and let Circle and Rectangle inherit from it.
- Less repetition: color is defined only once in Shape.
- Easier maintenance: If we add border_color, we modify just one place.
- More flexible: If we add a Triangle class, it automatically gets color and describe().

```python
class Shape: 
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"This is a {self.color} shape."
```

::right::

&nbsp;

````md magic-move
<<< @/snippets/DRY_v2.py python
````

---
layout: two-cols
class: large-python-motion
---

## Inheritance

Inheritance is useful when:
- There existst a “is a type of” relationship between two “real-world” objects
- There is more than one “child” object
- Each “child” should expose the full “parent” (public) interface

<br> 

```python
class Shape: 
    def __init__(self, color):
        self.color = color

    def describe(self):
        return f"This is a {self.color} shape."
```

::right::

&nbsp;

```python
class Circle(Shape):  
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        return f"This is a {self.color} circle 
                with radius {self.radius}."

class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color)  
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"This is a {self.color} rectangle with
                width {self.width} and height {self.height}."
```
---
layout: two-cols
class: large-python-motion
---

## Python vs C++ | Inheritance

<br>

### Python

```python
class Polygon:
    def __init__( self, nverts ):
        self.nverts = nverts

    def area( self ):
        raise NotImplementedError

class Square( Polygon ):
    def __init__( self, size ):
        self.__size = size
        Polygon.__init__( self, nverts=4 )

    def area( self ):
        return self.__size**2
```

- Baseclass methods optional, up to the programmer

::right::

&nbsp;

### C++

```c
class Polygon {
    public:
    Polygon( int _nverts ) {nverts = _nverts;}
    virtual float area();
    int nverts;
}

class Square : public Polygon {
    public:
    Square( int _size ) : Polygon(4) {size = _size}
    float area() {
    return size * size;
    }

private:
    float size;
}
```

- Baseclass methods enforced through the ‘virtual’ keyword