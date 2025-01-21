class Henkilö:
    def __init__(self, nimi) -> None:
        self._nimi = nimi
    
    # Getter
    def get_nimi(self):
        return self._nimi
    
    # Setter
    def set_nimi(self, uusi_nimi):
        if uusi_nimi == '':
            raise ValueError('Nimi ei saa olla tyhjä')
        else:
            self._nimi = uusi_nimi

henkilö = Henkilö('Matti')
print(henkilö.get_nimi())   # Matti
henkilö.set_nimi('Maija')
print(henkilö.get_nimi())   # Maija
henkilö.set_nimi('')        # Virhe!!! 