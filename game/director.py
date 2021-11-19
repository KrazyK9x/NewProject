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
        # self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.scene.get_sprite_list("Walls"))

        self.player_sprite = player.player_maker()
        self.player_list.append(self.player_sprite)
        self.player_sprite.center_x = 1000 // 2
        self.player_sprite.center_y = 1000 // 2


        # Variables for changing the camera:
        # *****************************************************************************************
        # Camera bounding box around player
        self.top = self.player_sprite.center_y + 200
        self.bottom = self.player_sprite.center_y - 200
        self.right = self.player_sprite.center_x + 300
        self.left = self.player_sprite.center_x - 300

        # Overall screen/room size
        # Used for ensuring camera bounds don't go negative (A.K.A set room size)
        self.right_boundary = 1000
        self.left_boundary = 0
        self.top_boundary = 1000
        self.bottom_boundary = 0

        #Starting position for the view
        self.left_view = 100
        self.bottom_view = 200
        self.right_view = self.left_view + constants.SCREEN_WIDTH
        self.top_view = self.bottom_view + constants.SCREEN_HEIGHT

        # This sets starting view
        arcade.set_viewport(self.left_view, self.right_view, self.bottom_view, self.top_view)
        # *****************************************************************************************
        

    def on_show(self):
        arcade.set_background_color(arcade.color.PUCE_RED)
        
        self.window.set_mouse_visible(False)
    
    def draw_grid(self):
        for i in range(0, 1000, 25):
            arcade.draw_line(i, 0, i, 1000, arcade.color.BLACK, 1)
        for i in range(0, 1000, 25):
            arcade.draw_line(0, i, 1000, i, arcade.color.BLACK, 1)

    def on_draw(self):
        arcade.start_render()

        # Draw grid
        self.draw_grid()

        # Display all Characters
        self.player_list.draw()
        
    
    def on_update(self, delta_time):
        # Calculate speed based on the keys pressed
        self.player_sprite.change_x = 0
        self.player_sprite.change_y = 0

        # Move player but keep him inside room boundaries
        if self.up_pressed and not self.down_pressed and self.player_sprite.top < self.top_boundary:
            self.player_sprite.change_y = constants.CHARACTER_SPEED
        elif self.down_pressed and not self.up_pressed and self.player_sprite.bottom > self.bottom_boundary:
            self.player_sprite.change_y = -constants.CHARACTER_SPEED
        if self.left_pressed and not self.right_pressed and self.player_sprite.left > self.left_boundary:
            self.player_sprite.change_x = -constants.CHARACTER_SPEED
        elif self.right_pressed and not self.left_pressed and self.player_sprite.right < self.right_boundary:
            self.player_sprite.change_x = constants.CHARACTER_SPEED



        # Call update to move the sprite
        # If using a physics engine, call update player to rely on physics engine
        # for movement, and call physics engine here.
        # self.physics_engine.update()
        self.player_list.update()
        self.player_list.update_animation()

        # This handles moving the view (camera)
        self.scroll()

        # This is used to time measurements later
        # self.time_taken += delta_time
        
    def scroll(self):
        # Reset Variable to False
        changed = False
        
        # Moves entire view/window around room baoundaries
        # and moves player scroll boundaries around view/window

        # Change Camera Left
        if self.left_view <= self.left_boundary: # If the view hits the boundary of the room, STOP moving camera
            pass
        elif self.player_sprite.left < self.left: # Else, update view and player scroll boundary
            self.left -= constants.CHARACTER_SPEED
            self.right -= constants.CHARACTER_SPEED
            self.left_view -= constants.CHARACTER_SPEED
            self.right_view -= constants.CHARACTER_SPEED
            changed = True
        
        # Change Camera Right
        if self.right_view >= self.right_boundary:
            pass
        elif self.player_sprite.right > self.right:
            self.left += constants.CHARACTER_SPEED
            self.right += constants.CHARACTER_SPEED
            self.left_view += constants.CHARACTER_SPEED
            self.right_view += constants.CHARACTER_SPEED
            changed = True
            
        # Change Camera Top
        if self.top_view >= self.top_boundary:
            pass
        elif self.player_sprite.top > self.top:
            self.top += constants.CHARACTER_SPEED
            self.bottom += constants.CHARACTER_SPEED
            self.top_view += constants.CHARACTER_SPEED
            self.bottom_view += constants.CHARACTER_SPEED
            changed = True

        # Change Camera Bottom
        if self.bottom_view <= self.bottom_boundary:
            pass
        elif self.player_sprite.bottom < self.bottom:
            self.top -= constants.CHARACTER_SPEED
            self.bottom -= constants.CHARACTER_SPEED
            self.top_view -= constants.CHARACTER_SPEED
            self.bottom_view -= constants.CHARACTER_SPEED
            changed = True

        # If changed is true, update viewport to new scene
        if changed:
            arcade.set_viewport(self.left_view,
                                self.right_view,
                                self.bottom_view,
                                self.top_view)


# Keyboard bindings:
# *****************************************************************************************
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
# *****************************************************************************************