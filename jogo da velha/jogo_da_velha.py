import numpy as np
from os import system
from math import inf
import time
import pygame as pg

pg.init()
matrix = ["-","-","-","-","-","-","-","-","-"]
human , o = 'o' , 'o'
ai , x = 'x' , 'x'

# PARTE GRÁFICA 

# DIMENSÕES
height = 500
width = 400
# CORES
black = (0,0,0)
white=(255,255,255)
# COORDENADAS PARA OS 'X' e 'Y'
x_pos1 = width/3+30
x_pos2 = width/3*2+30
y_pos1 = height/3+30
y_pos2 = height/3*2+30
line = (10,10,10)
# CRIANDO A INTERFACE
win = pg.display.set_mode((width,height))
fps = 30
CLOCK = pg.time.Clock()
pg.display.set_caption("JOGO DA VELHA")
# CARREGANDO IMAGENS
starting = pg.image.load('velha.jpg')
x_photo = pg.image.load('X.png')
o_photo = pg.image.load('O.png')

starting = pg.transform.scale(starting,(width,height))
x_photo = pg.transform.scale(x_photo,(80,80))
o_photo = pg.transform.scale(o_photo,(80,80))


# FUNÇÃO PARA INICIAR
def starts():
    font = pg.font.SysFont('times new roman', 32 ,bold = True ,italic = True )
    text = font.render('Espere o jogador X jogar!', True, black, white)
    win.blit(starting,(0,0))
    pg.display.update()
    time.sleep(5)
    win.fill(white)
    center = ( 20,  height/ 2-10)
    win.blit(text, center)
    pg.display.update()
    time.sleep(1.5)
    win.fill(white)
# DESENHO DOS QUADRADOS
    pg.draw.line(win,line,(width/3 , 0),(width/3 , height),7)
    pg.draw.line(win,line,(width/3*2 ,0),(width/3*2 ,height),7)
    pg.draw.line(win,line,(0 ,height/3),(width , height/3),7)
    pg.draw.line(win,line,(0 ,height/3*2),(width , height/3*2),7)
    pg.display.update()
    time.sleep(1)


# PARTE DA IA
def check_winner():
    if matrix[0] == x and matrix[1] == x and matrix[2] == x:
        return x
    elif matrix[3] == x and matrix[4] == x and matrix[5] == x:
        return x
    elif matrix[6] == x and matrix[7] == x and matrix[8] == x:
        return x

    elif matrix[0] == x and matrix[3] == x and matrix[6] == x:
        return x
    elif matrix[1] == x and matrix[4] == x and matrix[7] == x:
        return x
    elif matrix[2] == x and matrix[5] == x and matrix[8] == x:
        return x

    elif matrix[0] == x and matrix[4] == x and matrix[8] == x:
        return x
    elif matrix[2] == x and matrix[4] == x and matrix[6] == x:
        return x


    elif matrix[0] == o and matrix[1] == o and matrix[2] == o:
        return o
    elif matrix[3] == o and matrix[4] == o and matrix[5] == o:
        return o
    elif matrix[6] == o and matrix[7] == o and matrix[8] == o:
        return o

    elif matrix[0] == o and matrix[3] == o and matrix[6] == o:
        return o
    elif matrix[1] == o and matrix[4] == o and matrix[7] == o:
        return o
    elif matrix[2] == o and matrix[5] == o and matrix[8] == o:
        return o

    elif matrix[0] == o and matrix[4] == o and matrix[8] == o:
        return o
    elif matrix[2] == o and matrix[4] == o and matrix[6] == o:
        return o
def minimax(matrix , depth , X):
    if check_winner() == x:
        score = 10
        return score
    if check_winner() == o:
        score = -10
        return score
    if space == 9:
        score = 0
        return score


    if X == True:
        best = -inf
        for i in range(len(matrix)):
            if matrix[i] == "-":
                matrix[i] = ai
                eval = minimax(matrix ,depth + 1 , False )
                matrix[i] = "-"
                best = max(best,eval)
        return best
    else:
        best = inf

        for i in range(len(matrix)):
            if matrix[i] == "-":
                matrix[i] = human
                eval = minimax(matrix ,depth +1 , True )
                best = min(eval,best)
                matrix[i] = "-"
        return best
    

def bestmove(matrix):
    bestval = -1000
    move = 0
    for i in range(len(matrix)):
        if matrix[i] != ai and matrix[i] != human:
            matrix[i] = ai
            moveval = minimax(matrix , 0 , False )
            matrix[i] = "-"
            if moveval > bestval :
                bestval = moveval
                move = i
    matrix[move] = ai
    if move == 0:
        win.blit(x_photo,(30,30))
        pg.display.update()
    elif move == 1:
        win.blit(x_photo,(x_pos1,30))
        pg.display.update()
    elif move == 2:
        win.blit(x_photo,(x_pos2,30))
        pg.display.update()
    elif move == 3:
        win.blit(x_photo,(30,y_pos1))
        pg.display.update()
    elif move == 4:
        win.blit(x_photo,(x_pos1,y_pos1))
        pg.display.update()
    elif move == 5:
        win.blit(x_photo,(x_pos2,y_pos1))
        pg.display.update()
    elif move == 6:
        win.blit(x_photo,(30,y_pos2))
        pg.display.update()
    elif move == 7:
        win.blit(x_photo,(x_pos1,y_pos2))
        pg.display.update()
    elif move == 8:
        win.blit(x_photo,(x_pos2,y_pos2))
        pg.display.update()


# PARTE DO JOGADOR

# TECLAS APERTADAS
def player():
    keys=pg.key.get_pressed()
    if keys[pg.K_KP1]:
        if matrix[0] != x and matrix[0] != o:
            matrix[0] = human
            win.blit(o_photo,(30,30))
            pg.display.update()
            return True
    elif keys[pg.K_KP2]:
        if matrix[1] != x and matrix[1] != o:
            matrix[1] = human
            win.blit(o_photo,(x_pos1,30))
            pg.display.update()
            return True
    elif keys[pg.K_KP3]:
        if matrix[2] != x and matrix[2] != o:
            matrix[2] = human
            win.blit(o_photo,(x_pos2,30))
            pg.display.update()
            return True
    elif keys[pg.K_KP4]:
        if matrix[3] != x and matrix[3] != o:
            matrix[3] = human
            win.blit(o_photo,(30,y_pos1))
            pg.display.update()
            return True
    elif keys[pg.K_KP5]:
        if matrix[4] != x and matrix[4] != o:
            matrix[4] = human
            win.blit(o_photo,(x_pos1,y_pos1))
            pg.display.update()
            return True
    elif keys[pg.K_KP6]:
        if matrix[5] != x and matrix[5] != o:
            matrix[5] = human
            win.blit(o_photo,(x_pos2,y_pos1))
            pg.display.update()
            return True
    elif keys[pg.K_KP7]:
        if matrix[6] != x and matrix[6] != o:
            matrix[6] = human
            win.blit(o_photo,(30,y_pos2))
            pg.display.update()
            return True
    elif keys[pg.K_KP8]:
        if matrix[7] != x and matrix[7] != o:
            matrix[7] = human
            win.blit(o_photo,(x_pos1,y_pos2))
            pg.display.update()
            return True
    elif keys[pg.K_KP9]:
        if matrix[8] != x and matrix[8] != o:
            matrix[8] = human
            win.blit(o_photo,(x_pos2,y_pos2))
            pg.display.update()
            return True

# VERIFICAÇÃO DE VITÓRIA
def check_winnerVF():
    if matrix[0] == x and matrix[1] == x and matrix[2] == x:
        pg.draw.line(win,line,(25,70),(width-25 ,70),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[3] == x and matrix[4] == x and matrix[5] == x:
        pg.draw.line(win,line,(25,240),(width-25 ,240),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[6] == x and matrix[7] == x and matrix[8] == x:
        pg.draw.line(win,line,(25,height-90),(width-25 ,height-90),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[0] == x and matrix[3] == x and matrix[6] == x:
        pg.draw.line(win,line,(75,35),(75,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[1] == x and matrix[4] == x and matrix[7] == x:
        pg.draw.line(win,line,(205,35),(205,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[2] == x and matrix[5] == x and matrix[8] == x:
        pg.draw.line(win,line,(width-60,35),(width-60,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[0] == x and matrix[4] == x and matrix[8] == x:
        pg.draw.line(win,line,(40,35),(width-30,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[2] == x and matrix[4] == x and matrix[6] == x:
        pg.draw.line(win,line,(width-30,35),(35,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return x
    elif matrix[0] == o and matrix[1] == o and matrix[2] == o:
        pg.draw.line(win,line,(25,70),(width-25 ,70),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[3] == o and matrix[4] == o and matrix[5] == o:
        pg.draw.line(win,line,(25,240),(width-25 ,240),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[6] == o and matrix[7] == o and matrix[8] == o:
        pg.draw.line(win,line,(25,height-90),(width-25 ,height-90),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[0] == o and matrix[3] == o and matrix[6] == o:
        pg.draw.line(win,line,(75,35),(75,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[1] == o and matrix[4] == o and matrix[7] == o:
        pg.draw.line(win,line,(205,35),(205,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[2] == o and matrix[5] == o and matrix[8] == o:
        pg.draw.line(win,line,(width-60,35),(width-60,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[0] == o and matrix[4] == o and matrix[8] == o:
        pg.draw.line(win,line,(40,35),(width-30,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    elif matrix[2] == o and matrix[4] == o and matrix[6] == o:
        pg.draw.line(win,line,(width-30,35),(35,height-55),7)
        pg.display.update()
        time.sleep(0.5)
        return o
    

# VERIFICAÇÃO DE ESPAÇOS VAZIOS
def space():
    j = 0
    for i in range(len(matrix)):
        if matrix[i] == x or matrix[i] == o :
            j += 1
    return j

def game_over(x):
    font = pg.font.SysFont('times new roman', 32 ,bold = True ,italic = True )
    if x == 1:
        text = font.render('X Venceu', True, black, white)
        center = ( width/ 2 - 50,  height/ 2-10)
        win.fill(white)
        win.blit(text, center)
        pg.display.update()
        time.sleep(5)
    elif x == 2:
        text = font.render('O Venceu', True, black, white)
        center = ( width/ 2 - 50,  height/ 2-10)
        win.fill(white)
        win.blit(text, center)
        pg.display.update()
        time.sleep(5)
    elif x == 3:
        text = font.render('Deu Velha!', True, black, white)
        center = ( width/ 2 - 50,  height/ 2-10)
        win.fill(white)
        win.blit(text, center)
        pg.display.update()
        time.sleep(5.0)


run = True
starts()
bestmove(matrix)
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            run = False
    if player() == True:
        pg.display.update()
        if space() == 9:
            game_over(3)
            pg.quit()
            run = False
        if check_winnerVF() == x:
            game_over(1)
            pg.quit()
            run = False
        if check_winnerVF() == o:
            game_over(2)
            pg.quit()
            run = False
        time.sleep(1)
        bestmove(matrix)
        time.sleep(0.5)
        if space() == 9:
            game_over(3)
            print(matrix)
            pg.quit()
            run = False
        if check_winnerVF() == x:
            game_over(1)
            pg.quit()
            run = False
        if check_winnerVF() == o:
            game_over(2)
            pg.quit()
            run = False
        time.sleep(1)


pg.quit()