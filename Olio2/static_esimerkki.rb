class Car:
    level = 0
    def __init__(self, brand: str, color: str, speed: int) -> None:
        self.brand = brand
        self.color = color
        self.speed = speed

    @staticmethod
    def hp_to_watts(hp):
        return hp * 745.699872
    
    @classmethod
    def update_level(cls, new_value):
        cls.level = new_value

audi = Car('Audi', 'red', 200)
skoda = Car('Skoda', 'Blue', 160)

print(Car.hp_to_watts(200))
Car.update_level(5)
audi.update_level(10)
skoda.update_level(15)

# Car.hp_to_watts(audi, 200) == audi.hp_to_watts(200)