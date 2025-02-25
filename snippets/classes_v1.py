class Shape:
    def __init__(self, color):
        self.color = color  # Attribute

    def describe(self):
        return f"This is a {self.color} shape."
    
# Creating an object (instance of Shape)
shape1 = Shape("red")

# Output: This is a red shape.
print(shape1.describe())  