class Car:
    level = 0
    def __init__(self, brand: str, color: str, speed: int) -> None:
        self.brand = brand
        self.color = color
        self.speed = speed

    def info(self):
        # print(f'Brand: {self.brand}\nColor: {self.color}\nSpeed: {self.speed}')
        return f'Brand: {self.brand}\nColor: {self.color}\nSpeed: {self.speed}'

audi = Car('Audi', 'red', 200)
skoda = Car('Skoda', 'Blue', 160)

print(audi.info())
audi.color = 'black'
print(audi.info())