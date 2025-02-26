import math

class Marble:
    def __init__(self, radius, material, id=None):
        self.radius = radius
        self.material = material
        self.id = id

    def volume(self):
        return 4/3*math.pi*self.radius**3
    
    def is_magnetic(self):
        return self.material.magnetic
    
    def mass(self):
        return self.volume()*self.material.density
    
    def get_serie_number(self):
        return self.id
    
glass = {'density': 2.5, 'magnetic': False}
steel = {'density': 8.05, 'magnetic': True}

M1 = Marble(radius=3.1, material=glass, id='G001')
M2 = Marble(radius=1.4, material=steel, id='S001')