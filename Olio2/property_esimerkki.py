class Henkilö:
    def __init__(self, nimi) -> None:
        self._nimi = nimi
    
    # Getter
    @property
    def name(self):
        return self._nimi
    
    # Setter
    @name.setter
    def name(self, uusi_nimi):
        if uusi_nimi:
            self._nimi = uusi_nimi
        else:
            raise ValueError('Nimi ei saa olla tyhjä')

henkilö = Henkilö('Matti')
print(henkilö.name)     # Matti
henkilö.name = 'Maija'
print(henkilö.name)     # Maija
try:
    henkilö.name = ''       # Virhe!!! 
except ValueError as e:
    print(e)
