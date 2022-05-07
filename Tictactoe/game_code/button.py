
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg

pg.init()

class Button():
    def __init__(self, x, y, img, size):
        width = img.get_width()
        height = img.get_height()
        self.img = pg.transform.scale(img, (int(width * size), int(height * size)))
        self.rect = self.img.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, surface):
        pos = pg.mouse.get_pos()
        active = False

        if pg.mouse.get_pressed()[0] == 1 and self.clicked == False:
            
            if self.rect.collidepoint(pos):

                self.clicked = True
                active = True
        
        if pg.mouse.get_pressed()[0] == 0:
            self.clicked = False


        surface.blit(self.img, (self.rect.x, self.rect.y))
        
        return active
        