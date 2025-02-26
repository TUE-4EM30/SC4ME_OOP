import math

class Circle:
  def __init__(self, radius, shape):
    self.shape  = shape
    self.radius = radius

  def area(self):
    return math.pi*self.radius**2

  def tell_color(self):
    return self.shape.tell_color()
  
class Rectangle:
  def __init__(self, color, width, height):
    self.color = color
    self.width = width
    self.height = height

  def area(self):
    return self.width*self.height

  def tell_color(self):
    return self.shape.tell_color()