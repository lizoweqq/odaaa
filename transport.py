class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        print(f"{self.brand} {self.model}")


class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def info(self):
        print(f"{self.brand} {self.model}, дверей: {self.doors}")


class Bike(Vehicle):
    def __init__(self, brand, model, bike_type):
        super().__init__(brand, model)
        self.bike_type = bike_type

    def info(self):
        print(f"{self.brand} {self.model}, тип: {self.bike_type}")


class Truck(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def info(self):
        print(f"{self.brand} {self.model}, вантажопідйомність: {self.capacity} т")


car1 = Car("Toyota", "Corolla", 4)
bike1 = Bike("Giant", "Talon 3", "гірський")
truck1 = Truck("MAN", "TGX", 18)

car1.info()
bike1.info()
truck1.info()