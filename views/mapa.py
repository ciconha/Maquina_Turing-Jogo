import arcade
import random
from models.carta import Carta

SIMBOLOS_GREGOS = ["α", "β", "γ", "δ"]

class MapaView(arcade.View):
    def __init__(self):
        super().__init__()
        self.usuario_cartas = []
        self.computador_cartas = []
        self.fita_mt = []
        self.simbolo_alvo = ""
        self.rodada = 1
        self.usuario_pontos = 0
        self.computador_pontos = 0
        self.resultado_rodadas = []
        self.jogo_finalizado = False

        self.setup()

    def setup(self):
        self.usuario_cartas = [Carta(simbolo, 150 + i * 120, 150) for i, simbolo in enumerate(SIMBOLOS_GREGOS)]
        self.computador_cartas = [Carta(simbolo, 150 + i * 120, 500) for i, simbolo in enumerate(SIMBOLOS_GREGOS)]
        self.gerar_fita()

    def gerar_fita(self):
        self.fita_mt = [random.choice(["0", "1"]) for _ in range(8)]
        self.simbolo_alvo = random.choice(SIMBOLOS_GREGOS)

    def on_draw(self):
        arcade.start_render()

        # Fita MT
        arcade.draw_text("Fita MT:", 800, 600, arcade.color.BLACK, 16)
        for i, bit in enumerate(self.fita_mt):
            arcade.draw_text(bit, 800, 570 - i * 20, arcade.color.BLUE, 14)

        # Rodada e pontuação
        arcade.draw_text(f"Rodada: {self.rodada}", 50, 650, arcade.color.BLACK, 18)
        arcade.draw_text(f"Usuário: {self.usuario_pontos:.2f} pts", 50, 620, arcade.color.GREEN, 16)
        arcade.draw_text(f"Computador: {self.computador_pontos:.2f} pts", 50, 600, arcade.color.RED, 16)
        arcade.draw_text(f"Símbolo alvo: {self.simbolo_alvo}", 50, 570, arcade.color.DARK_RED, 16)

        # Cartas
        for carta in self.usuario_cartas:
            desenhar_carta(carta.x, carta.y, carta.simbolo, arcade.color.LIGHT_GREEN)

        for carta in self.computador_cartas:
            desenhar_carta(carta.x, carta.y, carta.simbolo, arcade.color.LIGHT_CORAL)

        # Resultado final
        if self.jogo_finalizado:
            arcade.draw_text("JOGO FINALIZADO", 400, 350, arcade.color.BLACK, 24, anchor_x="center")
            vencedor = "Empate"
            if self.resultado_rodadas.count("usuario") > self.resultado_rodadas.count("computador"):
                vencedor = "Usuário venceu!"
            elif self.resultado_rodadas.count("computador") > self.resultado_rodadas.count("usuario"):
                vencedor = "Computador venceu!"
            arcade.draw_text(vencedor, 400, 320, arcade.color.DARK_BLUE, 20, anchor_x="center")

    def on_mouse_press(self, x, y, button, modifiers):
        if self.jogo_finalizado:
            return

        for carta in self.usuario_cartas:
            if abs(x - carta.x) < 50 and abs(y - carta.y) < 70:
                self.jogada(carta.simbolo)
                break

    def jogada(self, simbolo_usuario):
        simbolo_computador = random.choice(SIMBOLOS_GREGOS)

        # Verifica acerto
        if simbolo_usuario == self.simbolo_alvo:
            self.usuario_pontos += 0.5
        else:
            self.usuario_pontos -= 0.5

        if simbolo_computador == self.simbolo_alvo:
            self.computador_pontos += 0.5
        else:
            self.computador_pontos -= 0.5

        # Atualiza fita
        self.gerar_fita()

        # Verifica fim da rodada
        if self.usuario_pontos >= 2 or self.computador_pontos >= 2:
            vencedor = "empate"
            if self.usuario_pontos > self.computador_pontos:
                vencedor = "usuario"
            elif self.computador_pontos > self.usuario_pontos:
                vencedor = "computador"

            self.resultado_rodadas.append(vencedor)
            self.rodada += 1
            self.usuario_pontos = 0
            self.computador_pontos = 0

            if len(self.resultado_rodadas) == 3:
                if self.resultado_rodadas.count("usuario") == 1 and self.resultado_rodadas.count("computador") == 1:
                    self.rodada = 4
                else:
                    self.jogo_finalizado = True
            elif len(self.resultado_rodadas) == 4:
                self.jogo_finalizado = True

def desenhar_carta(x, y, simbolo, cor_fundo):
    arcade.draw_rectangle_filled(x, y, 100, 140, arcade.color.BLACK)
    arcade.draw_rectangle_filled(x, y, 96, 136, cor_fundo)
    arcade.draw_text(simbolo, x, y, arcade.color.BLACK, 24, anchor_x="center", anchor_y="center")
