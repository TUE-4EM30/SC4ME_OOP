class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):  # Extending Animal class
    def speak(self):
        return "Bark!"

my_dog = Dog()

# Output: Bark!
print(my_dog.speak())  