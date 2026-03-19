import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 800

class GoodCoin(arcade.Sprite):
    def update(self, delta_time=1/60):
        self.center_y -= 2
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT
            self.center_x = random.randrange(SCREEN_WIDTH)

class BadCoin(arcade.Sprite):
    def update(self, delta_time=1/60):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0 or self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 or self.top > SCREEN_HEIGHT:
            self.change_y *= -1

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.good_coin_list = None
        self.bad_coin_list = None
        self.coin_list = None

        self.sonido_moneda = arcade.load_sound("bien.mp3")
        self.sonido_error = arcade.load_sound("error.mp3")

        self.player_sprite = None
        self.score = 0
        
        self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.good_coin_list = arcade.SpriteList()
        self.bad_coin_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.score = 0

        self.player_sprite = arcade.Sprite("jugador.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            good_coin = GoodCoin("enemigo.png", SPRITE_SCALING_COIN)
            bad_coin = BadCoin("bad.png", SPRITE_SCALING_COIN)
            
            bad_coin.change_x = random.choice([-3, 3])
            bad_coin.change_y = random.choice([-3, 3])

            good_coin.center_x = random.randrange(SCREEN_WIDTH)
            good_coin.center_y = random.randrange(SCREEN_HEIGHT)
            bad_coin.center_x = random.randrange(SCREEN_WIDTH)
            bad_coin.center_y = random.randrange(SCREEN_HEIGHT)
            
            self.coin_list.append(good_coin)
            self.coin_list.append(bad_coin)
            self.good_coin_list.append(good_coin)
            self.bad_coin_list.append(bad_coin)

    def on_draw(self):
        self.clear()

        self.coin_list.draw()
        self.player_list.draw()
        
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.good_coin_list) == 0:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 
                             arcade.color.WHITE, 50, anchor_x="center")

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.good_coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def on_update(self, delta_time):
        if len(self.good_coin_list) > 0:
            self.coin_list.update()

            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.good_coin_list)
            for good_coin in coins_hit_list:
                good_coin.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.sonido_moneda)
                
            coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_coin_list)
            for bad_coin in coins_hit_list:    
                bad_coin.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.sonido_error)

def main():
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()