import math

class Shape:
  def __init__(self, color):
    self.color = color

  def tell_color(self):
    return f'This is a {self.color} shape.'

class Circle:
  def __init__(self, radius, shape):
    self.shape  = shape
    self.radius = radius

  def area(self):
    return math.pi*self.radius**2

  def tell_color(self):
    return self.shape.tell_color()