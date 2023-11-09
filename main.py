class Vehicle:
    def __init__(self, make, model, year, weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight

    def display_info(self):
        return(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg")

    def honk(self):
        print("beep beep")

class Car(Vehicle):
    def __init__(self, make, model, year, weight, num_doors):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nDoors: {self.num_doors}")

    def honk(self):
        print("beep beep")

class Boat(Vehicle):
    def __init__(self, make, model, year, weight, boat_type):
        super().__init__(make, model, year, weight)
        self.boat_type = boat_type

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nType: {self.boat_type}")

    def honk(self):
        print("oooooo")

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, num_doors, payload_capacity):
        super().__init__(make, model, year, weight)
        self.num_doors = num_doors
        self.payload_capacity = payload_capacity

    def display_info(self):
        print(f"Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nWeight: {self.weight} kg\nDoors: {self.num_doors}\nCapacity: {self.payload_capacity}")

    def honk(self):
        print("honk")

    def dump_load(self):
        print("errrrr...")

if __name__ == "__main__":
    # Create instances of Vehicle Car
    car = Car("Toyota", "Corolla", 2021, 1275.0, 4)
    truck= Truck("Mac", "Street 750", 2019, 220.0, 2, 2000) #<--- but this now takes truck's constructor.

    # Display information of the car
    print("Car Info:")
    car.display_info()
    car.honk()
    print()


    # Display information of the motorcycle
    print("Truck Info:")
    truck.display_info()
    truck.honk()
    print()

    # Show total number of vehicles created, if you are going for the Bonus
    # print(f"Total number of vehicles: {Vehic;e.number_of_vehicles}")