from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("City Runner - by ChiragAgg5k")
clock = pygame.time.Clock()

# Please set relative path to these files yourself. These are set for my system and 100% wont work on yours

skySurface = pygame.image.load(
    "ActualCodingSTUFF/Python Stuff/Python-Games/City Runner - PyGame/Image Files/runnerBg.png").convert()
pathSurface = pygame.image.load(
    "ActualCodingSTUFF/Python Stuff/Python-Games/City Runner - PyGame/Image Files/RunnerPath.png").convert()
textSurface = pygame.image.load(
    "ActualCodingSTUFF/Python Stuff/Python-Games/City Runner - PyGame/Image Files/text.png").convert_alpha()
textRectangle = textSurface.get_rect(center=(400, 60))

playerSurface = pygame.image.load(
    "ActualCodingSTUFF/Python Stuff/Python-Games/City Runner - PyGame/Image Files/Player2.png").convert_alpha()
playerRectangle = playerSurface.get_rect(topleft=(0, 200))

while True:

    for event in pygame.event.get():

        # checking quit button
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(skySurface, (0, 0))
    screen.blit(pathSurface, (0, 300))
    screen.blit(playerSurface, playerRectangle)

    if playerRectangle.x < 350:
        playerRectangle.x += 4

    screen.blit(textSurface, textRectangle)

    mousePos = pygame.mouse.get_pos()
    if playerRectangle.collidepoint(mousePos):
        print(pygame.mouse.get_pressed())

    # updating our screen
    pygame.display.update()

    # setting max frame rate = 60
    clock.tick(60)
