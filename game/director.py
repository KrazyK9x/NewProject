from game import constants
from game import player
import arcade

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        #Variables and stuff
        # self.wall_list = None
        self.player_list = None

        self.player_sprite = None

        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        # self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        ## This is for making a solitary character
        # image_source = "game/assets/graphics/basic_char.png"
        # self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        # self.player_sprite.center_x = constants.SCREEN_WIDTH // 2
        # self.player_sprite.center_y = constants.SCREEN_HEIGHT // 2
        # self.player_list.append(self.player_sprite)
        # self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))

        self.player_sprite = player.player_maker()
        
        self.player_list.append(self.player_sprite)

    def on_show(self):
        arcade.set_background_color(arcade.color.PUCE_RED)
        
        self.window.set_mouse_visible(False)
    
    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
    
    def on_update(self, delta_time):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        if self.up_pressed and not self.down_pressed:
            self.player_sprite.change_y = constants.CHARACTER_SPEED
        elif self.down_pressed and not self.up_pressed:
            self.player_sprite.change_y = -constants.CHARACTER_SPEED
        if self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -constants.CHARACTER_SPEED
        elif self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = constants.CHARACTER_SPEED

        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        self.player_list.update()
        self.player_list.update_animation()

        # self.time_taken += delta_time
        
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False