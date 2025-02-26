import math

class Shape: 
  def __init__(self, color):
    self.color = color

  def tell_color(self):
    return f'This is a {self.color} shape.'

class Circle(Shape):  
  def __init__(self, color, radius):
    super().__init__(color)
    self.radius = radius

  def area(self):
    return math.pi*self.radius**2
  
  # create a circle
  red_circle = Circle('red', 5)

  # print the color of the circle
  print(red_circle.tell_color())