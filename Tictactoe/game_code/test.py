import os
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg
    
file = 'start_img.png'

a = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
b = os.path.join(a, "images", "start_img.png")
pg.image.load(b)
 

