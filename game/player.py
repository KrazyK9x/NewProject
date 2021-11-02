# image file
# frame location, x and y
# frame size, width and height
# number of frames
import arcade
from game import constants

def player_maker():
        
    player_sprite = arcade.AnimatedWalkingSprite(scale=constants.CHARACTER_SCALING)

    player_sprite.stand_right_textures = []
    for i in range(10):
        player_sprite.stand_right_textures.append(arcade.load_texture("game/assets/graphics/warriorspritesheet.png", x=i*32, y=0, width=32, height=32))
    
    player_sprite.stand_left_textures = []
    for i in range(10):
        player_sprite.stand_left_textures.append(arcade.load_texture("game/assets/graphics/warriorspritesheet.png", x=i*32, y=0, width=32, height=32, mirrored=True))

    player_sprite.walk_right_textures = []
    for i in range(10):
        player_sprite.walk_right_textures.append(arcade.load_texture("game/assets/graphics/warriorspritesheet.png", x=i*32, y=64, width=32, height=32))
    
    player_sprite.walk_left_textures = []
    for i in range(10):
        player_sprite.walk_left_textures.append(arcade.load_texture("game/assets/graphics/warriorspritesheet.png", x=i*32, y=64, width=32, height=32, mirrored=True))
    
    return player_sprite