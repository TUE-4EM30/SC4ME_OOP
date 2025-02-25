class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        # Delegating engine-related tasks
        self.engine = Engine()  

    def start(self):
        # Delegating start to Engine
        return self.engine.start()  

my_car = Car()

# Output: Engine started
print(my_car.start())  