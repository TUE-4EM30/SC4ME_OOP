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