# Base class
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def power_on(self):
        print(f"{self.brand} {self.model} is powering on.")

# Inherited class
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        # Call the base class constructor
        super().__init__(brand, model)
        self.storage = storage
        self.battery = battery  # in mAh
    
    def take_photo(self):
        print(f"{self.brand} {self.model} takes a photo 📸")
    
    def show_specs(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery: {self.battery}mAh")
# Base class
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Derived classes
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")

# List of vehicles
vehicles = [Car(), Plane(), Boat()]

# Demonstrating polymorphism
for v in vehicles:
    v.move()


# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 4000)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 5000)

# Using methods
phone1.power_on()
phone1.take_photo()
phone1.show_specs()

print()  # Just for spacing
phone2.power_on()
phone2.take_photo()
phone2.show_specs()
