class Dog:
    def sound(self):
        return "Woof!"

class Cat:
    def sound(self):
        return "Meow!"

class Bird:
    def sound(self):
        return "Chirp!"

dog = Dog()
cat = Cat()
bird = Bird()

print(dog.sound())
print(cat.sound())
print(bird.sound())