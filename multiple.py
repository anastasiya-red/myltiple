class Vehicle:
    vehicle_type = "none"


class Car:
    price = 1000000

    def __init__(self, horsepower = 100):
        self.horsepower = horsepower

    def horse_powers(self):
        return f'У Car лошадиных сил {self.horsepower}'


class Nissan(Vehicle, Car):
    price = 3000000
    vehicle_type = '4wd'

    def horse_powers(self):
        print(super().horse_powers())
        print(f'У Nissan лошадиных сил {self.horsepower}')



murano = Nissan()
print(murano.vehicle_type, murano.price)
print()

murano.horse_powers()






