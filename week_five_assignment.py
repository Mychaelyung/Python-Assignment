# Activity 1: Design Your Own Class!
# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery = battery

    def make_call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"{self.brand} {self.model} charged to {self.battery}%")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage}GB, Battery: {self.battery}%)"


# Child class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)
        self.cooling_system = cooling_system

    def play_game(self, game):
        if self.battery > 20:
            self.battery -= 10
            print(f"Playing {game} on {self.brand} {self.model} 🎮 (Battery: {self.battery}%)")
        else:
            print("Battery too low to play games!")

    # Overriding method (polymorphism)
    def charge(self, amount):
        super().charge(amount)
        print(f"Cooling system {self.cooling_system} is keeping the phone cool while charging.")

# Example usage
phone1 = Smartphone("Samsung", "S23", 256, 80)
gaming_phone = GamingPhone("Asus", "ROG 6", 512, 20, "Liquid Cooling")

print(phone1)
phone1.make_call("08012345678")
phone1.charge(25)

print("\n" + str(gaming_phone))
gaming_phone.play_game("PUBG")
gaming_phone.charge(81)


# Activity 2: Polymorphism Challenge!
class Vehicle:
    def move(self):
        pass  # abstract idea (to be overridden)


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")


# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
