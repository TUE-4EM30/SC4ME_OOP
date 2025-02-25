class Shape:
    def __init__(self, color):
        self.set_color(color)

    def describe(self):
        return f"This is a {self.__color} shape."
    
    def set_color(self, new_color):
        assert isinstance(new_color, str), 
            "Color must be a string."
        self.__color = new_color

# Creating an object (instance of Shape)
shape1 = Shape("red")

# Changing color to blue
shape1.set_color("blue")

# Output: This is a blue shape.
print(shape1.describe())  
