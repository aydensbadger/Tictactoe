from button import Button
from label import Label
from Easy import easy
from mod import question
from Medium import medium
from Hard import hard
from mod import put_numbers_on_screen_2
from mod import score_divider
import time
import os
import pathlib
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg

images_path = pathlib.Path(__file__).parents[1] / "images"
game_code_path = pathlib.Path(__file__).parents[1] / "game_code"
game_code_path = str(game_code_path) + '\score.txt'

pg.init()

width = 800
height = 500

BLACK = (17, 17, 17)

surface = pg.display.set_mode((width, height))  
surface.fill(BLACK)

def stats():
    
    total_img = pg.image.load(images_path / "total_img.png")
    easy_img = pg.image.load(images_path / "easy_img.png")
    medium_img = pg.image.load(images_path / "medium_img.png")
    hard_img = pg.image.load(images_path / "hard_img.png")
    total_wins_img = pg.image.load(images_path / "total_wins_img.png")
    total_loses_img = pg.image.load(images_path / "total_loses_img.png")
    total_ties_img = pg.image.load(images_path / "total_ties_img.png")
    total_wlr_img = pg.image.load(images_path / "total_wlr_img.png")
    total_tpo_img = pg.image.load(images_path / "total_tpo_img.png")
    total_tpx_img = pg.image.load(images_path / "total_tpx_img.png")
    total_tpr_img = pg.image.load(images_path / "total_tpr_img.png")
    easy_wins_img = pg.image.load(images_path / "easy_wins_img.png")
    easy_loses_img = pg.image.load(images_path / "easy_loses_img.png")
    easy_ties_img = pg.image.load(images_path / "easy_ties_img.png")
    easy_wlr_img = pg.image.load(images_path / "easy_wlr_img.png")
    easy_tpo_img = pg.image.load(images_path / "easy_tpo_img.png")
    easy_tpx_img = pg.image.load(images_path / "easy_tpx_img.png")
    easy_tpr_img = pg.image.load(images_path / "easy_tpr_img.png")
    medium_wins_img = pg.image.load(images_path / "medium_wins_img.png")
    medium_loses_img = pg.image.load(images_path / "medium_loses_img.png")
    medium_ties_img = pg.image.load(images_path / "medium_ties_img.png")
    medium_wlr_img = pg.image.load(images_path / "medium_wlr_img.png")
    medium_tpo_img = pg.image.load(images_path / "medium_tpo_img.png")
    medium_tpx_img = pg.image.load(images_path / "medium_tpx_img.png")
    medium_tpr_img = pg.image.load(images_path / "medium_tpr_img.png")
    hard_wins_img = pg.image.load(images_path / "hard_wins_img.png")
    hard_loses_img = pg.image.load(images_path / "hard_loses_img.png")
    hard_ties_img = pg.image.load(images_path / "hard_ties_img.png")
    hard_wlr_img = pg.image.load(images_path / "hard_wlr_img.png")
    hard_tpo_img = pg.image.load(images_path / "hard_tpo_img.png")
    hard_tpx_img = pg.image.load(images_path / "hard_tpx_img.png")
    hard_tpr_img = pg.image.load(images_path / "hard_tpr_img.png")
    back_img = pg.image.load(images_path / "back_img.png")

    back_button = Button(20, 425, back_img, 2.7)

    total_label = Label(total_img, 3.5)
    easy_label = Label(easy_img, 3.5)
    medium_label = Label(medium_img, 3.5)
    hard_label = Label(hard_img, 3.5)

    total_wins_label = Label(total_wins_img, 2.5)
    total_loses_label = Label(total_loses_img, 2.5)
    total_ties_label = Label(total_ties_img, 2.5)
    total_wlr_label = Label(total_wlr_img, 2.5)
    total_tpo_label = Label(total_tpo_img, 2.5)
    total_tpx_label = Label(total_tpx_img, 2.5)
    total_tpr_label = Label(total_tpr_img, 2.5)

    easy_wins_label = Label(easy_wins_img, 2.5)
    easy_loses_label = Label(easy_loses_img, 2.5)
    easy_ties_label = Label(easy_ties_img, 2.5)
    easy_wlr_label = Label(easy_wlr_img, 2.5)
    easy_tpx_label = Label(easy_tpx_img, 2.5)
    easy_tpo_label = Label(easy_tpo_img, 2.5)
    easy_tpr_label = Label(easy_tpr_img, 2.5)
    
    medium_wins_label = Label(medium_wins_img, 2.5)
    medium_loses_label = Label(medium_loses_img, 2.5)
    medium_ties_label = Label(medium_ties_img, 2.5)
    medium_wlr_label = Label(medium_wlr_img, 2.5)
    medium_tpx_label = Label(medium_tpx_img, 2.5)
    medium_tpo_label = Label(medium_tpo_img, 2.5)
    medium_tpr_label = Label(medium_tpr_img, 2.5)
    
    hard_wins_label = Label(hard_wins_img, 2.5)
    hard_loses_label = Label(hard_loses_img, 2.5)
    hard_ties_label = Label(hard_ties_img, 2.5)
    hard_wlr_label = Label(hard_wlr_img, 2.5)
    hard_tpx_label = Label(hard_tpx_img, 2.5)
    hard_tpo_label = Label(hard_tpo_img, 2.5)
    hard_tpr_label = Label(hard_tpr_img, 2.5)

    score_divider(0, 1, 3)
    score_divider(7, 8, 10)
    score_divider(14, 15, 17)
    score_divider(21, 22, 24)
    
    running = True  
    
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        if back_button.draw(surface):
            surface.fill(BLACK)
            return 

        total_label.draw(18, 20, surface)
        easy_label.draw(211, 20, surface)
        medium_label.draw(408, 20, surface)
        hard_label.draw(602, 20, surface)

        total_wins_label.draw(18, 77, surface)
        total_loses_label.draw(18, 127, surface)
        total_ties_label.draw(18, 177, surface)
        total_wlr_label.draw(18, 227, surface)
        total_tpx_label.draw(18, 277, surface)
        total_tpo_label.draw(18, 327, surface)
        total_tpr_label.draw(18, 377, surface)

        easy_wins_label.draw(211, 77, surface)
        easy_loses_label.draw(211, 127, surface)
        easy_ties_label.draw(211, 177, surface)
        easy_wlr_label.draw(211, 227, surface)
        easy_tpx_label.draw(211, 277, surface)
        easy_tpo_label.draw(211, 327, surface)
        easy_tpr_label.draw(211, 377, surface)

        medium_wins_label.draw(408, 77, surface)
        medium_loses_label.draw(408, 127, surface)
        medium_ties_label.draw(408, 177, surface)
        medium_wlr_label.draw(408, 227, surface)
        medium_tpx_label.draw(408, 277, surface)
        medium_tpo_label.draw(408, 327, surface)
        medium_tpr_label.draw(408, 377, surface)

        hard_wins_label.draw(602, 77, surface)
        hard_loses_label.draw(602, 127, surface)
        hard_ties_label.draw(602, 177, surface)
        hard_wlr_label.draw(602, 227, surface)
        hard_tpx_label.draw(602, 277, surface)
        hard_tpo_label.draw(602, 327, surface)
        hard_tpr_label.draw(602, 377, surface)
        
        list_x_total = [0, 1, 2, 3, 4, 5, 6]
        list_x_easy = [7, 8, 9, 10, 11, 12, 13]
        list_x_medium = [14, 15, 16, 17, 18, 19, 20]
        list_x_hard = [21, 22, 23, 24, 25, 26, 27]

        list_y_1 = [0, 7, 14, 21]
        list_y_2 = [1, 8, 15, 22]
        list_y_3 = [2, 9, 16, 23]
        list_y_4 = [3, 10, 17, 24]
        list_y_5 = [4, 11, 18, 25]
        list_y_6 = [5, 12, 19, 26]
        list_y_7 = [6, 13, 20, 27]

        file = 'start_img.png'
        for num in range(28):

            with open(game_code_path, 'r') as f:
                data = f.read()

            lines = data.splitlines()
            score = str(lines[num]) 

            if num in list_x_total:
                x = 110
            elif num in list_x_easy:
                x = 303
            elif num in list_x_medium:
                x = 500
            elif num in list_x_hard:
                x = 694

            if num in list_y_1:
                y = 80
            elif num in list_y_2:
                y = 130
            elif num in list_y_3:
                y = 180
            elif num in list_y_4:
                y = 230
            elif num in list_y_5:
                y = 277
            elif num in list_y_6:
                y = 380
            elif num in list_y_7:
                y = 330

            for i, letter in enumerate(score):
                if put_numbers_on_screen_2(i, letter, surface, x, y) == '-7.2':
                    x -= 7.2

        pg.display.update()

def start_game():

    easy_img = pg.image.load(images_path / "easy1_img.png") 
    medium_img = pg.image.load(images_path / "medium1_img.png")
    hard_img = pg.image.load(images_path / "hard1_img.png")
    difficulty_img = pg.image.load(images_path / "difficulty_img.png")
    back_img = pg.image.load(images_path / "back_img.png")

    easy_button = Button(30, 290, easy_img, 5)
    medium_button = Button(285, 290, medium_img, 5)
    hard_button = Button(540, 290, hard_img, 5)
    difficulty_label = Label(difficulty_img, 8)
    back_button = Button(30, 415, back_img, 2.7)

    running = True

    while running:
        surface.fill(BLACK)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
    
        difficulty_label.draw(115, 20, surface)
        
        if medium_button.draw(surface): 
            time.sleep(0.2)
            while True:
                
                if question(surface, 2) == 1:
                    surface.fill(BLACK)
                    time.sleep(0.2) 

                    if medium(surface, 1): continue
                    else: break
            
                else:
                    surface.fill(BLACK)
                    time.sleep(0.2)

                    if medium(surface, 2): continue
                    else: break
            
        if hard_button.draw(surface): 
            time.sleep(0.2)
            while True:
                
                if question(surface, 3) == 1:
                    surface.fill(BLACK)
                    time.sleep(0.2)

                    if hard(surface, 1): continue
                    else: break
            
                else:
                    surface.fill(BLACK)
                    time.sleep(0.2)

                    if hard(surface, 2): continue
                    else: break
 
        if easy_button.draw(surface): 
            time.sleep(0.2)
            while True:
                
                if question(surface, 1) == 1:
                    surface.fill(BLACK)
                    time.sleep(0.2)

                    if easy(surface, 1): continue
                    else: break
            
                else:   
                    surface.fill(BLACK) 
                    time.sleep(0.2)

                    if easy(surface, 2): continue
                    else: break

        if back_button.draw(surface):
            surface.fill(BLACK)
            running = False

        pg.display.update()
        
def main():
    pg.display.set_caption('TicTacToe')

    start_img = pg.image.load(images_path / "start_img.png")
    exit_img = pg.image.load(images_path / "exit_img.png")
    title_img = pg.image.load(images_path / "title_img.png")
    stats_img = pg.image.load(images_path / "stats_img.png")
    
    stats_button = Button(110, 325, stats_img, 7)
    start_button = Button(260,175, start_img, 7)
    exit_button = Button(415, 325, exit_img, 7)
    title_label = Label(title_img, 8)

    running = True 
  
    while running:   

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        if start_button.draw(surface): 
            surface.fill(BLACK)
            start_game()

        if stats_button.draw(surface): 
            surface.fill(BLACK)
            stats()

        title_label.draw(145, 20, surface)
            
        if exit_button.draw(surface):
            running = False
  
        pg.display.update()
 
if __name__ == '__main__': main()


