import random

class Baralho:
    def __init__(self, cartas):
        self.cartas = cartas.copy()
        random.shuffle(self.cartas)

    def comprar(self):
        if self.cartas:
            return self.cartas.pop()
        return None
