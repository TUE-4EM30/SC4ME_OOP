class Shape:
    def __init__(self, color, opacity):
        self.color = color  # Attribute
        self.opacity = opacity  # Attribute

    def describe(self):
        return f"This is a {self.color} shape 
                    with {self.opacity} opacity."
    
    def set_color(self, new_color):
        self.color = new_color
    
# Creating an object (instance of Shape)
shape1 = Shape("red",0.8)

# Changing color to blue
shape1.set_color("blue")

# Output: This is a blue shape with 0.8 opacity.
print(shape1.describe())  