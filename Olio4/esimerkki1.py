class Moottori:
    def käynnistää(self):
        print('Moottori käynnistyy')

class Auto():
    def __init__(self) -> None:
        self._moottori = Moottori()

    def käynnistää(self):
        self._moottori.käynnistää()
        print('Auto käynnistyy')

auto = Auto()
auto.käynnistää()