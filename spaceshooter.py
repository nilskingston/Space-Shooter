"""
spaceshooter.py
Author: Nils Kingston
Credit: <list sources used, if any>

Assignment:
Write and submit a program that implements the spacewar game:
https://github.com/HHS-IntroProgramming/Spacewar
"""
from ggame import App, RectangleAsset, ImageAsset, SoundAsset
from ggame import LineStyle, Color, Sprite, Sound

 SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

black = Color(0x000000, 1)

noline = LineStyle(0, black)
bg_asset = RectangleAsset(SCREEN_WIDTH, SCREEN_HEIGHT, noline, black)
bg = Sprite(bg_asset, (0,0))




myapp = App(SCREEN_WIDTH, SCREEN_HEIGHT)
myapp.run()