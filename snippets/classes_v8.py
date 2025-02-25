class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

class Laptop:
    def __init__(self, brand, battery_capacity):
        self.brand = brand
        # Composition: Laptop "has a" Battery
        self.battery = Battery(battery_capacity)  

    def describe(self):
        return f"{self.brand} laptop with 
            {self.battery.capacity}mAh battery"

my_laptop = Laptop("Dell", 5000)

# Output: Dell laptop with 5000mAh battery
print(my_laptop.describe())  