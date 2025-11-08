from math import pi

class Cercle:
    def __init__(self, rayon: float):
        if rayon <= 0:
            raise ValueError("Le rayon doit etre positif et non nul.")
        self._rayon = rayon

    def get_rayon(self):
        return self._rayon

    def set_rayon(self, valeur: float):
        if valeur <= 0:
            raise ValueError("Le rayon doit etre positif et non nul.")
        self._rayon = valeur

    def perimetre(self):
        return 2 * pi * self._rayon

    def surface(self):
        return pi * self._rayon ** 2

    def agrandir(self, pourcentage: float):
        self._rayon *= (1 + pourcentage / 100)
