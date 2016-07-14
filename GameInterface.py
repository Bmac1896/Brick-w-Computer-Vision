import pygame


# Authors: Brandon McDonald & Alex Brooks
# Date: 7/13/2016
# Compiler Interepereter: 2.7.12

pygame.init()

#----------Variables------------
black = (0, 0, 0)
deep_purple = (175, 50, 200)

frame_width = 1000
frame_height = 650
blockWidth = 150
blockHeight = 20
blockXPos = frame_width/2 - blockWidth/2
blockYPos = frame_height - blockHeight - 20
blockXPos_change = 0


clock = pygame.time.Clock()
#-------------GUI Configurations------------

gameDisplay = pygame.display.set_mode((frame_width, frame_height))

pygame.display.set_caption('Brick')

pygame.display.update()

gameExit = False
#recentKey = None
#--------------GameLoop-------------------
while not gameExit:
    for event in pygame.event.get():
        #print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                blockXPos_change = -5
            if event.key == pygame.K_RIGHT:
                blockXPos_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                blockXPos_change = 0
            if event.key == pygame.K_RIGHT:
                blockXPos_change = 0


    blockXPos += blockXPos_change

    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay, deep_purple, [blockXPos, blockYPos, blockWidth,
                                                blockHeight])
    pygame.display.update()

    clock.tick(60)


pygame.quit()
quit()
