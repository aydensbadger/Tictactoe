from button import Button
from label import Label
import time
import random
import pathlib
from mod import put_numbers_on_screen
from mod import win_check
from mod import score_editor
import contextlib
with contextlib.redirect_stdout(None):
    import pygame as pg

pg.init()

images_path = pathlib.Path(__file__).parents[1] / "images"
game_code_path = pathlib.Path(__file__).parents[1] / "game_code"
game_code_path = str(game_code_path) + '\score.txt'

def easy_com(com, board):
    global top_L_open, top_R_open, top_open, middle_open, bottem_open, bottem_L_open, bottem_R_open, left_open, right_open 

    if com == 1: enemy = 2
    else: enemy = 1
    num = random.randint(1, 9)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            
        num = random.randint(1, 9)

        if num == 1 and top_L_open: 
            board[0][0] = com

            return board

        elif num == 2 and top_open: 
            board[0][1] = com

            return board

        elif num == 3 and top_R_open:
            board[0][2] = com

            return board

        elif num == 4 and left_open:
            board[1][0] = com

            return board

        elif num == 5 and middle_open: 
            board[1][1] = com

            return board

        elif num == 6 and right_open: 
            board[1][2] = com

            return board

        elif num == 7 and bottem_L_open: 
            board[2][0] = com

            return board

        elif num == 8 and bottem_open: 
            board[2][1] = com

            return board

        elif num == 9 and bottem_R_open: 
            board[2][2] = com

            return board

        if top_open:
            board[0][1] = com
                
            return board

        elif left_open:
            board[1][0] = com

            return board

        elif right_open:
            board[1][2] = com

            return board

        elif bottem_open:
            board[2][1] = com

            return board

        elif bottem_L_open:
            board[2][0] = com

            return board
        
        elif top_L_open:
            board[0][0] = com

            return board
        
        elif top_R_open:
            board[0][2] = com

            return board
        
        elif bottem_R_open:
            board[2][2] = com

            return board
        
        elif middle_open:
            board[1][1] = com
                
            return board

def easy(surface, player):
    global top_L_open, top_R_open, top_open, middle_open, bottem_open, bottem_L_open, bottem_R_open, left_open, right_open 
    
    tile_img = pg.image.load(images_path / "tile_img.png")
    board_img = pg.image.load(images_path / "board_img.png")
    x_img = pg.image.load(images_path / "x_img.png")
    circle_img = pg.image.load(images_path / "circle_img.png")
    tie_img = pg.image.load(images_path / "tie_img.png")
    play_again_img = pg.image.load(images_path / "play_again_img.png")
    back_img = pg.image.load(images_path / "back_img.png")
    you_lose_img = pg.image.load(images_path / "you_lose_img.png")
    you_win_img = pg.image.load(images_path / "you_win_img.png")
    you_img = pg.image.load(images_path / "you_img.png")
    com_img = pg.image.load(images_path / "com_img.png")
    backround_win_img = pg.image.load(images_path / "backround_win_img.png")
    backround_lose_img = pg.image.load(images_path / "backround_lose_img.png")
    backround_tie_img = pg.image.load(images_path / "backround_tie_img.png")
    easy_img = pg.image.load(images_path / "easy_img.png")
    line_img = pg.image.load(images_path / "line_img.png")
    line2_img = pg.image.load(images_path / "line2_img.png")
    
    you_label = Label(you_img, 5.9)
    com_label = Label(com_img, 5.9)
    backround_win_label = Label(backround_win_img, 11)
    backround_lose_label = Label(backround_lose_img, 11)
    backround_tie_label = Label(backround_tie_img, 11)
    easy_label = Label(easy_img, 5.4)
    you_win_label = Label(you_win_img, 6 )
    you_lose_label = Label(you_lose_img, 6)
    tie_label = Label(tie_img, 6)
    play_again_button = Button(325, 295, play_again_img, 3.6)
    back_button = Button(237, 295, back_img, 2.4)

    top_L_button = Button(18, 3, tile_img, 14.6)
    top_R_button = Button(352, 3, tile_img, 14.6)
    top_button = Button(185, 3, tile_img, 14.6)
    middle_button = Button(185, 169, tile_img, 14.6)
    bottem_button = Button(185, 337, tile_img, 14.6)
    bottem_L_button = Button(18, 337, tile_img, 14.6)
    bottem_R_button = Button(352, 337, tile_img, 14.6)
    left_button = Button(18, 169, tile_img, 14.6)
    right_button = Button(352, 169, tile_img, 14.6)
    
    board_label = Label(board_img, 15.2)
    line_label = Label(line_img, 16)
    line2_label = Label(line2_img, 15.8)

    x_label_1 = Label( x_img, 9.5)
    x_label_2 = Label( x_img, 9.5)
    x_label_3 = Label( x_img, 9.5)
    x_label_4 = Label( x_img, 9.5)
    x_label_5 = Label( x_img, 9.5)
    x_label_6 = Label( x_img, 9.5)
    x_label_7 = Label( x_img, 9.5)
    x_label_8 = Label( x_img, 9.5)
    x_label_9 = Label( x_img, 9.5)

    circle_label_1 = Label(circle_img, 9.5)
    circle_label_2 = Label(circle_img, 9.5)
    circle_label_3 = Label(circle_img, 9.5)
    circle_label_4 = Label(circle_img, 9.5)
    circle_label_5 = Label(circle_img, 9.5)
    circle_label_6 = Label(circle_img, 9.5)
    circle_label_7 = Label(circle_img, 9.5)
    circle_label_8 = Label(circle_img, 9.5)
    circle_label_9 = Label(circle_img, 9.5)

    top_L_open = True
    top_R_open = True
    top_open = True
    middle_open = True
    bottem_open = True
    bottem_L_open = True
    bottem_R_open = True
    left_open = True
    right_open = True
    won = False
    
    if player == 1: com = 2
    else: com = 1
    slow = 1 
    turn = 1
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    BLACK = (17, 17, 17)

    com_label.draw(514, 285, surface)
    you_label.draw(514, 95, surface)
    board_label.draw(0, 0, surface)
    easy_label.draw(528, 5, surface)
    line_label.draw(784, 0, surface)
    line2_label.draw(516.7, 485, surface)

    running = True    

    if player == 1:
        score_editor('plus', 11)
    if player == 2:  
        score_editor('plus', 12)

    with open(game_code_path, 'r') as f:
            data = f.read()

    lines = data.splitlines()
    score = str(lines[28]) 
    
    for i, letter in enumerate(score):
        put_numbers_on_screen(i, letter, score, surface, 620, 190)
    
    with open(game_code_path, 'r') as f:
            data = f.read()

    lines = data.splitlines()
    score = str(lines[29]) 
    
    for i, letter in enumerate(score):
        put_numbers_on_screen(i, letter, score, surface, 620, 385)
        
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        if turn == player and not won:
            if top_L_button.draw(surface) and top_L_open:
                if turn == 1: 
                    turn = 2
                    board[0][0] = 1
                else:
                    turn = 1
                    board[0][0] = 2

            if top_R_button.draw(surface) and top_R_open:
                if turn == 1: 
                    turn = 2
                    board[0][2] = 1
                else:
                    turn = 1
                    board[0][2] = 2
                    
            if top_button.draw(surface) and top_open:
                if turn == 1: 
                    turn = 2
                    board[0][1] = 1
                else:
                    turn = 1
                    board[0][1] = 2
            
            if middle_button.draw(surface) and middle_open:
                if turn == 1: 
                    turn = 2 
                    board[1][1] = 1
                else:
                    turn = 1
                    board[1][1] = 2

            if bottem_button.draw(surface) and bottem_open:
                if turn == 1: 
                    turn = 2
                    board[2][1] = 1
                else:
                    turn = 1
                    board[2][1] = 2

            if bottem_L_button.draw(surface) and bottem_L_open:
                if turn == 1: 
                    turn = 2
                    board[2][0] = 1
                else:
                    turn = 1
                    board[2][0] = 2

            if bottem_R_button.draw(surface) and bottem_R_open:
                if turn == 1: 
                    turn = 2
                    board[2][2] = 1
                else:
                    turn = 1 
                    board[2][2] = 2
                
            if left_button.draw(surface) and left_open:
                if turn == 1: 
                    turn = 2
                    board[1][0] = 1
                else:
                    turn = 1
                    board[1][0] = 2

            if right_button.draw(surface) and right_open:
                if turn == 1: 
                    turn = 2
                    board[1][2] = 1
                else:
                    turn = 1
                    board[1][2] = 2

        if board[0][0] == 1:
            top_L_open = False
            x_label_1.draw(22, 9, surface)

        if board[0][1] == 1:
            top_open = False
            x_label_2.draw(189, 9, surface)

        if board[0][2] == 1:
            top_R_open = False
            x_label_3.draw(357, 9, surface)

        if board[1][0] == 1:
            left_open = False
            x_label_4.draw(22, 175, surface)

        if board[1][1] == 1:
            middle_open = False
            x_label_5.draw(189, 175, surface)

        if board[1][2] == 1:
            right_open = False
            x_label_6.draw(357, 175, surface)

        if board[2][0] == 1:
            bottem_L_open = False
            x_label_7.draw(22, 341, surface)

        if board[2][1] == 1:
            bottem_open = False
            x_label_8.draw(189, 341, surface)

        if board[2][2] == 1:
            bottem_R_open = False
            x_label_9.draw(357, 341, surface)

        if board[0][0] == 2:
            top_L_open = False
            circle_label_1.draw(22, 9, surface)

        if board[0][1] == 2:
            top_open = False
            circle_label_2.draw(189, 9, surface)

        if board[0][2] == 2:
            top_R_open = False
            circle_label_3.draw(357, 9, surface)

        if board[1][0] == 2:
            left_open = False
            circle_label_4.draw(22, 175, surface)

        if board[1][1] == 2:
            middle_open = False
            circle_label_5.draw(189, 175, surface)

        if board[1][2] == 2:
            right_open = False
            circle_label_6.draw(357, 175, surface)

        if board[2][0] == 2:
            bottem_L_open = False
            circle_label_7.draw(22, 341, surface)

        if board[2][1] == 2:
            bottem_open = False
            circle_label_8.draw(189, 341, surface)

        if board[2][2] == 2:
            bottem_R_open = False
            circle_label_9.draw(357, 341, surface)

        if win_check(1, board):
            won = True
            slow += 1

            if slow == 100:
                if player == 1:
            
                    score_editor('plus', 0)
                    score_editor('plus', 7)
                    score_editor('plus', 28)
                    
                    backround_win_label.draw(210, 140, surface)
                    you_win_label.draw(252.5, 160, surface)

                    while True:

                        for event in pg.event.get():    
                            if event.type == pg.QUIT:
                                pg.quit()   

                        if play_again_button.draw(surface):
                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return True
                        
                        if back_button.draw(surface):

                            score_editor('reset', 28)
                            score_editor('reset', 29)

                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return False
                        
                        pg.display.update() 
                
                else:
                    score_editor('plus', 1)
                    score_editor('plus', 8)
                    score_editor('plus', 29)

                    backround_lose_label.draw(210, 140, surface)
                    you_lose_label.draw(252.5, 160, surface)

                    while True:

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()
                        

                        if play_again_button.draw(surface):
                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return True
                        
                        if back_button.draw(surface):

                            score_editor('reset', 28)
                            score_editor('reset', 29)

                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return False
                        
                        pg.display.update() 
            
        elif win_check(2, board):
            won = True
            slow += 1

            if slow == 100:
                if player == 2:

                    score_editor('plus', 0)
                    score_editor('plus', 7)
                    score_editor('plus', 28)

                    backround_win_label.draw(210, 140, surface)
                    you_win_label.draw(252.5, 160, surface)

                    while True:

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()

                        if play_again_button.draw(surface):
                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return True
                        
                        if back_button.draw(surface):

                            score_editor('reset', 28)
                            score_editor('reset', 29)

                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return False
                        
                        pg.display.update() 
                else:

                    score_editor('plus', 1)
                    score_editor('plus', 8)
                    score_editor('plus', 29)

                    backround_lose_label.draw(210, 140, surface)
                    you_lose_label.draw(252.5, 160, surface)

                    while True:

                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                pg.quit()

                        if play_again_button.draw(surface):
                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return True
                        
                        if back_button.draw(surface):
                            
                            score_editor('reset', 28)
                            score_editor('reset', 29)

                            time.sleep(0.2)
                            surface.fill(BLACK)
                            return False
                        
                        pg.display.update() 

        else:
            c = 0               
            for row in board:
                for i in row:
                    if i != 0:
                        c += 1
                        if c == 9:
                            run = True
                            slow = 0
                            while run:
                                slow += 1
                                if slow == 8000000: run = False
                                
                            score_editor('plus', 2)
                            score_editor('plus', 9)

                            backround_tie_label.draw(210, 140, surface)
                            tie_label.draw(252.5, 160, surface)

                            while True:

                                for event in pg.event.get():
                                    if event.type == pg.QUIT:
                                        pg.quit()

                                if play_again_button.draw(surface):
                                    time.sleep(0.2)
                                    surface.fill(BLACK)
                                    return True

                                if back_button.draw(surface):

                                    score_editor('reset', 28)
                                    score_editor('reset', 29)

                                    time.sleep(0.2)
                                    surface.fill(BLACK)
                                    return False

                                pg.display.update() 
                
                        continue
                    else: break
                                            
        if not won:
            if turn == 1 and com == 1 or turn == 2 and com == 2:
                if turn == 1:
                    board = easy_com(com, board)
                    turn = 2
                    
                elif turn == 2:
                    board = easy_com(com, board)
                    turn = 1

        pg.display.update()    
