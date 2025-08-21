# views/menu.py

import arcade
from config import SCREEN_WIDTH, SCREEN_HEIGHT
from views.mapa import MapaView



class MenuView(arcade.View):
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("MT - Menu Inicial", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50,
                         arcade.color.WHITE, 24, anchor_x="center")
        arcade.draw_text("Pressione ENTER para começar", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                         arcade.color.GRAY, 16, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.ENTER:
            mapa_view = MapaView()
            self.window.show_view(mapa_view)
