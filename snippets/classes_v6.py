class Shape:
    def __init__(self, color):
        self.set_color(color)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__color})"
    
    def set_color(self, new_color):
        assert isinstance(new_color, str), "Color must be a string."
        self.__color = new_color

# Creating an object (instance of Shape)
shape1 = Shape("red")

# Output: Shape(red)
print(shape1)