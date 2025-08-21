import arcade

class JogoView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Rodada 1: Monte sua fita!", 250, 550, arcade.color.YELLOW, 20)
        # Aqui você vai desenhar cartas, tempo, avatar, etc.
