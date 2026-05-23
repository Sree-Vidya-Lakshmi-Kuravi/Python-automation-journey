### OOPS

## Vehicle Inheritance
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def display_info(self):
        print("Vehicle brand:", self.brand)
        print("Vehicle speed:", self.speed)

class Car(Vehicle):
    def __init__(self, brand, speed, fuel_type):
        super().__init__(brand, speed)
        self.fuel_type = fuel_type

    def display_car_info(self):
        print("Fuel Type:", self.fuel_type)


class Bike(Vehicle):
    def __init__(self, brand, speed, bike_type):
        super().__init__(brand, speed)
        self.bike_type = bike_type

    def display_bike_type(self):
        print("Bike Type:", self.bike_type)

# b1 = Bike("GT", "160kmph", "diesel")
# b1.display_info()
# b1.display_bike_type()

# c1 = Car("Lamborghini", "250kmph", "diesel")
# c1.display_info()
# c1.display_car_info()

# v1 = Vehicle("lamborghini", 264)
# print(v1.display_info())


## Animal System
class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        print("This animal makes sound")

class Dog(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    # def get_name(self):
    #     return self.name

    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def __init__(self, species, name):
        super().__init__(species)
        self.name = name

    # def get_name(self):
    #     return self.name

    def sound(self):
        print("Cat meows")


a1 = Animal("ani")
a1.sound()

d1 = Dog("Dog", "bochu_kukka")
print("Name:", d1.name)
d1.sound()

c1 = Cat("Cat", "thella_pilli")
print("Name:", c1.name)
c1.sound()

