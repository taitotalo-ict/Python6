class Car:
    def __init__(self, brand: str, color: str, speed: int) -> None:
        self.brand = brand
        self.color = color
        self.speed = speed

    def info(self):
        # print(f'Brand: {self.brand}\nColor: {self.color}\nSpeed: {self.speed}')
        return f'Brand: {self.brand}\nColor: {self.color}\nSpeed: {self.speed}'

    def hp_to_watts(hp):
        return hp * 745.699872

audi = Car('Audi', 'red', 200)
skoda = Car('Skoda', 'Blue', 160)

# print(audi.info())
# audi.color = 'black'
# print(audi.info())

print(Car.hp_to_watts(200))

# Car.hp_to_watts(audi, 200) == audi.hp_to_watts(200)