class Vehicle:

    num_of_wheels = 4

    def __init__(self, make, model, fuel="gas"):
        self.make = make
        self.model = model
        self.fuel = fuel

    def __str__(self):
        return f"I drive {self.make} {self.model}. It runs on {self.fuel}"    

class Car(Vehicle):
    pass    

class Truck(Vehicle):
    num_of_wheels = 6

    def __init__(self, make, model, fuel="diesel"):
        super().__init__(make, model, fuel)
    

# car = Car("Maruti", "800")
# print(car);
        
truck = Truck("Tata", "407")
print(truck);
print(truck.num_of_wheels)

# print("for Class", Vehicle.num_of_wheels)
# print("for Object", car.num_of_wheels)

# car.num_of_wheels = 3
# print("for Class", Vehicle.num_of_wheels)
# print("for Object", car.num_of_wheels)