class Shape:
  def __init__(self, color):
    self.color = color  # Attribute

  def describe(self):
    return f"This is a {self.color} shape."
    
  def set_color(self, new_color):
    if isinstance(new_color, str):
      self.color = new_color
    elif isinstance(new_color, tuple):
      self.color = f'rgb{new_color}'

# Creating an object (instance of Shape)
shape1 = Shape("red")

# Changing color to blue
shape1.set_color("blue")

# Output: This is a blue shape.
print(shape1.describe())