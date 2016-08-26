import pygame, random, sys, time
from pygame.locals import *

pygame.init()

#color initialization
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
DARKRED = (128, 0, 0)
DARKBLUE = (0, 0, 128)
DARKGREEN = (0, 128, 0)
DARKYELLOW = (128, 128, 0)

#sets up the screen
screen_width = 350
screen_height = 350
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Simon Says')
screen.fill(WHITE)
pygame.display.update()

#set up for the squares
button_width = 150
button_height = 150

button_red = pygame.Rect(0,0, button_width, button_height)
button_blue = pygame.Rect(screen_width - button_width, 0, button_width, button_height)
button_green = pygame.Rect(screen_width - button_width, screen_height - button_height, button_width, button_height)
button_yellow = pygame.Rect(0, screen_height - button_height, button_width, button_height)

pygame.draw.rect(screen, RED, button_red)
pygame.draw.rect(screen, BLUE, button_blue)
pygame.draw.rect(screen, GREEN, button_green)
pygame.draw.rect(screen, YELLOW, button_yellow)

def reset():
    pygame.draw.rect(screen, RED, button_red)
    pygame.draw.rect(screen, BLUE, button_blue)
    pygame.draw.rect(screen, GREEN, button_green)
    pygame.draw.rect(screen, YELLOW, button_yellow)

GAMEOVER = False
count = 0;
clicks = 0;
clickPositions = []
rectSequence = []
randoms = []
sequence = []
clickSequence = []
log = []
colors = [DARKRED, DARKBLUE, DARKGREEN, DARKYELLOW]
regColors = ["RED","BLUE","GREEN","YELLOW"]

buttons = [button_red, button_blue, button_green, button_yellow]

pygame.display.update()

while not GAMEOVER:

    r = random.randint(0,3)
    randoms.append(r)
    sequence.append(colors[r])
    rectSequence.append(buttons[r])
    log.append(regColors[r])
    print(log)
    print(rectSequence)
    #print(randoms)

    for index,color in enumerate(sequence):
        time.sleep(.5)
        pygame.draw.rect(screen,color,buttons[randoms[index]])
        pygame.display.update()
        time.sleep(.5)
        reset()
        pygame.display.update()


    count += 1
    print("Count = ", count)

    #the click detection loop
    clicks = 0
    clickPositions = []
    while clicks < count:

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONUP:
                clicks += 1
                print("Clicks = ", clicks)
                clickPositions.append(pygame.mouse.get_pos())
                print(clickPositions)

    for index,shape in enumerate(rectSequence):
        if not shape.collidepoint(clickPositions[index]):
            print("BAD CLICK")
            GAMEOVER = True
        else:
            print("GOOD CLICK")







    #for event in pygame.event.get():
    #    if event.type == MOUSEBUTTONDOWN:

    #pygame.display.update()
    #reset()
