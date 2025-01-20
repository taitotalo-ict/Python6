class Car:
    def __init__(self, brand: str, color: str, speed: int) -> None:
        self.brand = brand
        self.color = color
        self.speed = speed
        self.info = f'Brand: {brand}\nColor: {color}\nSpeed: {speed}'
        self.info = 'Brand: ' + brand + '\nColor: ' + color + '\nSpeed: ' + str(speed)
        self.info = f'''
Brand: {brand}
Color: {color}
Speed: {speed}'''

audi = Car('Audi', 'red', 200)
skoda = Car('Skoda', 'Blue', 160)

print(audi.info)

print(skoda.info)