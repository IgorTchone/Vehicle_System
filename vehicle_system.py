class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def display(self):
        print("Brand:", self.brand)
        print("Year:", self.year)

class Car(Vehicle):
    def __init__(self, brand, year, num_doors):
        Vehicle.__init__(self, brand, year)
        self.num_doors = num_doors

    def display(self):
        Vehicle.display(self)
        print("Number of doors:", self.num_doors)

class Motorcycle(Vehicle):
    def __init__(self, brand, year, type_motorcycle):
        Vehicle.__init__(self, brand, year)
        self.type_motorcycle = type_motorcycle

    def display(self):
        Vehicle.display(self)
        print("Type of motorcycle:", self.type_motorcycle)

print("Enter 1 for Car or 2 for Motorcycle")
choice = input()

if choice == "1":
    brand = input("Enter the brand of the car: ")
    year = input("Enter the year of the car: ")
    num_doors = input("Enter the number of doors: ")

    car = Car(brand, year, num_doors)
    print()
    car.display()

elif choice == "2":
    brand = input("Enter the brand of the motorcycle: ")
    year = input("Enter the year of the motorcycle: ")
    type_motorcycle = input("Enter the type of motorcycle: ")

    motorcycle = Motorcycle(brand, year, type_motorcycle)
    print()
    motorcycle.display()

else:
    print("Invalid option")
