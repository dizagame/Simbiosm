import pygame
import os
from Player import x, y, width, height, speed
from Shopper import  xSh, ySh

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('!!!')

play = True
shopping = False

while play:
    pygame.time.delay(100)
    win.fill((0, 0, 0))

    if shopping == True:
        bgImg = pygame.image.load("cat.jpg")
        bgImg = pygame.transform.scale(bgImg, (500, 500))
        button1 = pygame.draw.rect(bgImg, (0, 255, 255), (xSh, ySh, width, height))
        button2 = pygame.draw.rect(bgImg, (0, 255, 255), (xSh, ySh, width, height))
        win.blit(bgImg, (0, 0))
        continue

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 15:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if keys[pygame.K_UP] and y > 15:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed


    shopper = pygame.draw.rect(win, (0, 255, 255), (xSh, ySh, width, height))
    player = pygame.draw.rect(win, (255, 20, 25), (x, y, width, height))


    if x >= xSh-(height//3) and y >= ySh-(height//2):
        pygame.Rect.copy(player)



    pygame.display.flip()
