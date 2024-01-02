class Vehicle :
    defaultName = "Maruti"
    defaultColor = "Golden"
    defaulWheelCount = 4

    def __init__(self, name = defaultName, color = defaultColor):
        self.name = name
        self.color = color

    def print_info(self):
        print("Name:", self.name)
        print("Color:", self.color)

    def get_num_of_wheels(cls):
        print(f"Number of wheels: {cls.defaulWheelCount}")

car = Vehicle()
car.print_info()