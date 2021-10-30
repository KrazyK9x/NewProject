from game import constants
import arcade

class StartView(arcade.View):
    def __init__(self):
        super().__init__()
        #Variables and stuff
        # self.wall_list = None
        self.player_list = None

        self.player_sprite = None
    
    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        # self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        image_source = "game/assets/graphics/basic_char.png"
        self.player_sprite = arcade.Sprite(image_source, constants.CHARACTER_SCALING)
        self.player_sprite.center_x = constants.SCREEN_WIDTH // 2
        self.player_sprite.center_y = constants.SCREEN_HEIGHT // 2
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally

    def on_show(self):
        arcade.set_background_color(arcade.color.PUCE_RED)
        
        self.window.set_mouse_visible(False)
    
    def on_draw(self):
        arcade.start_render()

        self.player_list.draw()
    
    def on_update(self, delta_time):
        pass
        # self.time_taken += delta_time
        