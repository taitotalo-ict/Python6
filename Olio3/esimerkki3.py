class Luokka1:
    def metodi1(self):
        print('Metodi1 luokasta Luokka1:sta')

class Luokka2:
    def metodi1(self):
        print('Metodi2 luokasta Luokka2:sta')

class LapsiLuokka(Luokka1, Luokka2):
    pass

olio = LapsiLuokka()
olio.metodi1()
# olio.metodi2()