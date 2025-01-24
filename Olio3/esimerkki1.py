class Eläin:
    def __init__(self, nimi) -> None:
        self.nimi = nimi
    
    def ääntele(self):
        print(f'{self.nimi} ääntelee.')

class Koira(Eläin):
    def __init__(self, nimi, rotu):
        super().__init__(nimi)
        self.rotu = rotu

    def ääntele(self):
        print(f'{self.nimi} ({self.rotu}) haukkuu.')

class Kissa(Eläin):
    def ääntele(self):
        print(f'{self.nimi} maukuu.')

koira = Koira('Rex', 'Labradorinnoutaja')
koira.ääntele()

kissa = Kissa('Felix')
kissa.ääntele()
