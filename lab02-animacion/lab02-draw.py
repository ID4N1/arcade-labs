import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
contador = 0
class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mi Juego")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
    
    def on_draw(self):
        self.clear()
        # Poner aquí el código del dibujo
        arcade.draw.draw_circle_filled(200, 150, 50, arcade.color.BLACK)
        arcade.draw.draw_circle_filled(400, 150, 50, arcade.color.BLACK)
        arcade.draw.draw_circle_filled(200, 150, 25, arcade.color.ALMOND)
        arcade.draw.draw_circle_filled(400, 150, 25, arcade.color.ALMOND)
        arcade.draw.draw_lbwh_rectangle_filled(100, 175,450,150, arcade.color.COOL_GREY)
        arcade.draw.draw_lbwh_rectangle_filled(500, 275,50,50, arcade.color.BLACK)
        arcade.draw.draw_lbwh_rectangle_filled(500, 175,50,50, arcade.color.BLACK)
        arcade.draw.draw_lbwh_rectangle_filled(525, 275,25,25, arcade.color.YELLOW)
        arcade.draw.draw_lbwh_rectangle_filled(525, 175,25,25, arcade.color.YELLOW)
        # Cambiar la posición y/o tamaño del dibujo para crear animación
        

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()
