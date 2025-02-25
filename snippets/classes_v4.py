class Shape:
    def __init__(self, color, opacity):
        self.set_color(color)
        self.set_opacity(opacity)

    def describe(self):
        return f"This is a {self.__color} shape 
                    with {self.opacity} opacity."
    
    def set_color(self, new_color):
        assert isinstance(new_color, str), 
            "Color must be a string."
        self.__color = new_color

    def set_opacity(self, new_opacity):
        assert isinstance(new_opacity, float), 
            "Opacity must be a float."
        assert 0 <= new_opacity <= 1, 
            "Opacity must be between 0 and 1."
        self.__opacity = new_opacity

# Creating an object (instance of Shape)
shape1 = Shape("red",0.8)
 
