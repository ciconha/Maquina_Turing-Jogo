import random

NAIPES = ["♥", "♣", "♦", "♠"]
VALORES = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
CURINGAS = ["JOKER"]

def gerar_baralho():
    baralho = [f"{v}{n}" for v in VALORES for n in NAIPES]
    baralho += CURINGAS * 2
    random.shuffle(baralho)
    return baralho
