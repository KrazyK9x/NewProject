from game.director import StartView
from game import constants
import arcade


window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
window.set_update_rate(1/30) #frames per second
start_view = StartView()
start_view.setup()
window.show_view(start_view)
arcade.run()
