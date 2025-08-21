import arcade
from views.mapa import MapaView

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "MT - Máquina de Turnel"

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    mapa_view = MapaView()
    window.show_view(mapa_view)
    arcade.run()

if __name__ == "__main__":
    main()
