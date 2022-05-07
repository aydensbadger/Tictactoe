from button import Button
from label import Label
import random
import os
import contextlib
import pathlib
with contextlib.redirect_stdout(None):
    import pygame as pg
     
images_path = pathlib.Path(__file__).parents[1] / "images"
game_code_path = pathlib.Path(__file__).parents[1] / "game_code"
game_code_path = str(game_code_path) + '\score.txt'

BLACK = (17, 17, 17)

pg.init()

def put_numbers_on_screen_2(i, letter, surface, x, y):

    zero_img = pg.image.load(images_path / "zero_img.png")
    two_img = pg.image.load(images_path / "two_img.png")
    three_img = pg.image.load(images_path / "three_img.png")
    four_img = pg.image.load(images_path / "four_img.png")
    five_img = pg.image.load(images_path / "five_img.png")
    six_img = pg.image.load(images_path / "six_img.png")
    seven_img = pg.image.load(images_path / "seven_img.png")
    eight_img = pg.image.load(images_path / "eight_img.png")
    nine_img = pg.image.load(images_path / "nine_img.png")
    one_img = pg.image.load(images_path / "one_img.png")
    dot_img = pg.image.load(images_path / "dot_img.png")

    zero_label = Label(zero_img, 3.2)
    one_label = Label(one_img, 3.2)
    two_label = Label(two_img, 3.2)
    three_label = Label(three_img, 3.2)
    four_label = Label(four_img, 3.2)
    five_label = Label(five_img, 3.2)
    six_label = Label(six_img, 3.2)
    seven_label = Label(seven_img, 3.2)
    eight_label = Label(eight_img, 3.2)
    nine_label = Label(nine_img, 3.2)
    dot_label = Label(dot_img, 0.5)
 
    if letter == '.':
        x += 20
        y += 15.5
        dot_label.draw(x, y, surface)
        return '-7.2'
    else:
        for a in range(i):
            x += 20
    
    if letter == '1':
        one_label.draw(x, y, surface)
        return

    if letter == '2':
        two_label.draw(x, y, surface)
        return

    if letter == '3':
        three_label.draw(x, y, surface)
        return

    if letter == '4':
        four_label.draw(x, y, surface)
        return

    if letter == '5':
        five_label.draw(x, y, surface)
        return

    if letter == '6':
        six_label.draw(x, y, surface)
        return

    if letter == '7':
        seven_label.draw(x, y, surface)
        return

    if letter == '8':
        eight_label.draw(x, y, surface)
        return
        
    if letter == '9':
        nine_label.draw(x, y, surface)
        return

    if letter == '0':
        zero_label.draw(x, y, surface)
        return

def put_numbers_on_screen(i, letter, score, surface, x_1,  y_2):

    zero_img = pg.image.load(images_path / "zero_img.png")
    two_img = pg.image.load(images_path / "two_img.png")
    three_img = pg.image.load(images_path / "three_img.png")
    four_img = pg.image.load(images_path / "four_img.png")
    five_img = pg.image.load(images_path / "five_img.png")
    six_img = pg.image.load(images_path / "six_img.png")
    seven_img = pg.image.load(images_path / "seven_img.png")
    eight_img = pg.image.load(images_path / "eight_img.png")
    nine_img = pg.image.load(images_path / "nine_img.png")
    one_img = pg.image.load(images_path / "one_img.png")

    zero_label = Label(zero_img, 8)
    one_label = Label(one_img, 8)
    two_label = Label(two_img, 8)
    three_label = Label(three_img, 8)
    four_label = Label(four_img, 8)
    five_label = Label(five_img, 8)
    six_label = Label(six_img, 8)
    seven_label = Label(seven_img, 8)
    eight_label = Label(eight_img, 8)
    nine_label = Label(nine_img, 8)

    score = int(score)
    if score < 10: x, y = x_1, y_2
    elif score < 100 and score > 9: 
        if i == 0: x, y = x_1 - 30, y_2
        else: x, y = x_1 + 30, y_2
    elif score < 1000 and score > 99:
        if i == 0: x, y = x_1 - 55, y_2
        elif i == 1: x, y = x_1, y_2
        else: x, y = x_1 + 55, y_2
    else:
        while True:       
            print('HACKER ALERT')

    letter = int(letter)
    if letter == 1:
        one_label.draw(x, y, surface)
        return

    if letter == 2:
        two_label.draw(x, y, surface)
        return

    if letter == 3:
        three_label.draw(x, y, surface)
        return

    if letter == 4:
        four_label.draw(x, y, surface)
        return

    if letter == 5:
        five_label.draw(x, y, surface)
        return

    if letter == 6:
        six_label.draw(x, y, surface)
        return

    if letter == 7:
        seven_label.draw(x, y, surface)
        return

    if letter == 8:
        eight_label.draw(x, y, surface)
        return
        
    if letter == 9:
        nine_label.draw(x, y, surface)
        return

    if letter == 0:
        zero_label.draw(x, y, surface)
        return

def score_divider(line1, line2, line3):
    global file
    file = 'start_img'

    with open(game_code_path, 'r') as f:
        data = f.read()
        
    lines = data.splitlines()
    score1 = lines[line1]
    score2 = lines[line2]
    
    try: 
        score3 = int(score1) / int(score2)
    except ZeroDivisionError:
        score3 = 0
    
    score3 = round(score3, 2)
    lines[line3] = str(score3)
    data = '\n'.join(lines)

    with open(game_code_path, "w") as f:
        f.write(data)

    return

def score_editor(picker, line):
    if picker == 'plus':
        with open(game_code_path, 'r') as f:
            data = f.read()

        lines = data.splitlines()
        score = int(lines[line]) + 1
        lines[line] = str(score)
        data = '\n'.join(lines)

        with open(game_code_path, "w") as f:
            f.write(data)

        return
    
    elif picker == 'minus':
        with open(game_code_path, 'r') as f:
            data = f.read()

        lines = data.splitlines()
        score = int(lines[line]) - 1
        lines[line] = str(score)
        data = '\n'.join(lines)

        with open(game_code_path, "w") as f:
            f.write(data)

        return

    elif picker == 'reset':
        with open(game_code_path, 'r') as f:
            data = f.read()

        lines = data.splitlines()
        score = int(lines[line])
        score = int(0)
        lines[line] = str(score)
        data = '\n'.join(lines)

        with open(game_code_path, "w") as f:
            f.write(data)

        return 

    else:
        while True:
            print('Game crashed. Please contact support at: aydensbadger@gmail.com || IMPORTANT || PRESS: "ctrl+c" TO EXIT GAME.')

def win_check(shape, board):
    for row in board:
        for tile in row:
            if tile == shape:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == shape:
                continue
            else:
                break
        else:
            return True
    

    for tile in range(3):
        if board[tile][tile] == shape:
            continue
        else:
            break
    else:
        return True
    
    
    for tile in range(3):
        if board[tile][2-tile] == shape:
            continue
        else:
            break
    else:
        return True

def question(surface, difficulty):

    x_border_img = pg.image.load(images_path / "x_border_img.png")
    circle_border_img = pg.image.load(images_path / "circle_border_img.png")
    question_img = pg.image.load(images_path / "question_img.png")
    random_img = pg.image.load(images_path / "random_img.png")

    x_button = Button(100, 185, x_border_img, 9)
    circle_button = Button(555, 185, circle_border_img, 9)
    random_button = Button(245, 385, random_img, 7)
    question_label = Label(question_img, 12)

    surface.fill(BLACK)
    
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        question_label.draw(20, 20, surface)
        if x_button.draw(surface):
            score_editor('plus', 4)
                
            return 1

        if circle_button.draw(surface):
            score_editor('plus', 5)

            return 2
        
        if random_button.draw(surface):
            
            if difficulty == 1:
                score_editor('plus', 13)
            print(difficulty)
            if difficulty == 2:
                score_editor('plus', 20)
                
            if difficulty == 3:
                score_editor('plus', 27)
            
            if random.randint(1, 2) == 1: 
                score_editor('plus', 4)
                score_editor('plus', 6)
                return 1
            else: 
                score_editor('plus', 5)
                score_editor('plus', 6) 
                return 2

        pg.display.update() 


