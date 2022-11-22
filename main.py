# --- Imports --- #
import pygame
from pygame.locals import *

# --- Variables --- #
size = width,height = (1200,800)
road_w = int(width/1.6)
roadmark_w = int(width/80)

#starts pygame
pygame.init()

#turns on game loop
running = True

#screen size
screen = pygame.display.set_mode(size)
#window title
pygame.display.set_caption("Dylan's car game")
#background colour
screen.fill((220,80,210))

#draw road
pygame.draw.rect(
    screen,
    (50,50,50),
    (width/2-road_w/2, 0, road_w, height)
)

#black line in the middle
pygame.draw.rect(
    screen,
    (0,0,0),
    (width/2 - roadmark_w/2, 0, roadmark_w, height)
)

#white lines at the side
pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 - road_w/2 + roadmark_w * 2, 0, roadmark_w, height)
)
pygame.draw.rect(
    screen,
    (255,255,255),
    (width/2 + road_w/2 - roadmark_w * 3, 0, roadmark_w, height)
)

#updates display per frame
pygame.display.update()

#load sprites
car = pygame.image.load("car.png")
car_loc = car.get_rect()
car_loc.center = width/2 - road_w/4, height*0.8

#check for window close
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    screen.blit(car,car_loc)
    pygame.display.update()

#end
pygame.quit*()