""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
class Ball:
    def __init__(self, pos_x, pos_y, radio, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radio = radio
        self.color = color
        self.change_x = 0
        self.change_y = 0

    def draw(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.radio, self.color)

    def on_update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y

class outline:
    def __init__(self, pos_x, pos_y, radio, color):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.change_x = 0
        self.change_y = 0
        self.radio = radio
    def draw(self):
        arcade.draw_circle_outline(self.pos_x, self.pos_y,self.radio, self.color)

    def on_update(self):
        self.pos_x += self.change_x
        self.pos_y += self.change_y
        
class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def on_update(self, delta_time):
        self.ball.on_update()
        self.outline.on_update()
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.set_mouse_visible(False)
        # Aquí creas tu objeto Ball y lo guardas en self.ball
        self.ball = Ball(50, 50, 15, arcade.color.RED)
        self.outline = outline(50, 50,15, arcade.color.ALICE_BLUE)
    def on_draw(self):
        self.clear()
        # En lugar de usar la función de arcade directamente, 
        # llamamos al método draw() de TU objeto.
        self.ball.draw()
        self.outline.draw()
    
    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        # Cambiamos "self.draw.position_x" por el objeto real y sus atributos
        self.ball.pos_x = x
        self.ball.pos_y = y
    
    def on_mouse_press(self, x, y, button, modifiers):
        """ Called when the user presses a mouse button. """

        if button == arcade.MOUSE_BUTTON_LEFT:
            print("Left mouse button pressed at", x, y)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            print("Right mouse button pressed at", x, y)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.outline.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.outline.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.outline.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.outline.change_y = -MOVEMENT_SPEED
    
    def on_key_release(self, key, modifiers):
            """ Called whenever a user releases a key. """
            if key == arcade.key.LEFT or key == arcade.key.RIGHT:
                self.outline.change_x = 0
            elif key == arcade.key.UP or key == arcade.key.DOWN:
                self.outline.change_y = 0

    
def main():
    window = MyGame()
    arcade.run()

# Es una buena práctica en Python llamar a main() de esta manera:
if __name__ == "__main__":
    main()