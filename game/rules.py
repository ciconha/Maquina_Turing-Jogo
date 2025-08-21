class Rodada:
    def __init__(self):
        self.numero = 1
        self.pontuacao = { "jogador": 0, "computador": 0 }

    def verificar_vencedor(self):
        if self.numero == 3:
            if self.pontuacao["jogador"] > self.pontuacao["computador"]:
                return "Jogador venceu!"
            elif self.pontuacao["jogador"] < self.pontuacao["computador"]:
                return "Computador venceu!"
            else:
                return "Empate! Rodada extra!"
