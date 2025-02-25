class Circle:
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        return f"This is a {self.color} circle 
                with radius {self.radius}."

class Rectangle:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def describe(self):
        return f"This is a {self.color} rectangle with   
                width {self.width} and height {self.height}."