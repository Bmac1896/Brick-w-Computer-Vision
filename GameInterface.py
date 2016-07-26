import pygame
import time
import random
import math

# Authors: Brandon McDonald & Alex Brooks
# Date: 7/13/2016
# Compiler Interepereter: 2.7.12

pygame.init()

# ----------Non-Changing Variables------------
black = (0, 0, 0)
deep_purple = (175, 50, 200)
red = (255, 0, 0)
white = (255, 255, 255)
frame_width = 1000
frame_height = 650
blockWidth = 150
blockHeight = 20
paddleSpeed = 10
FPS = 30

clock = pygame.time.Clock()

# -------------GUI Configurations------------
gameDisplay = pygame.display.set_mode((frame_width, frame_height))

pygame.display.set_caption('Brick')

pygame.display.update()

# Message Function
font = pygame.font.SysFont(None, 25)


def message_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [frame_width / 4, frame_height / 2])


message_screen("Welcome! Raise Your Hand In Front Of Your Webcam To Begin!", deep_purple)
pygame.display.update()
time.sleep(3)


# --------------GameLoop-------------------
def gameLoop():
    # Changing Variables
    gameExit = False
    gameOver = False
    block_x_pos = frame_width / 2 - blockWidth / 2
    block_y_pos = frame_height - blockHeight - 20
    ball_x_pos = frame_width / 2
    ball_y_pos = frame_height - 100
    radius = 10
    block_x_change = 0
    ball_speed = 10
    ball_x_change = int(random.randrange(ball_speed - 1, ball_speed))
    ball_y_change = int(math.sqrt(math.pow(ball_speed, 2) - math.pow(ball_x_change, 2)))
    x_factor = 1 / math.pow(.5, 2)

    while not gameExit:

        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                gameExit = True

            # Paddle movement logic
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    block_x_change = -1 * paddleSpeed
                elif event.key == pygame.K_RIGHT:
                    block_x_change = paddleSpeed

            if event.type == pygame.KEYUP:
                block_x_change = 0
        block_x_pos += block_x_change

        # Boundaries for paddle
        if block_x_pos <= 0 or block_x_pos >= frame_width - blockWidth:
            block_x_change = 0

        # Ball movement logic
        if block_x_pos + blockWidth >= ball_x_pos >= block_x_pos and block_y_pos <= ball_y_pos + radius:
            paddle_percentage = ((float(ball_x_pos) - float(block_x_pos)) / float(blockWidth)) - 0.5
            ball_x_change = math.pow(paddle_percentage, 2) * ball_speed * x_factor
            if paddle_percentage < 0:
                ball_x_change *= -1
            ball_y_change = math.sqrt(math.pow(ball_speed, 2) - math.pow(ball_x_change, 2)) * -1
        if ball_y_pos - radius <= 0 or ball_y_pos + radius >= frame_height:
            ball_y_change *= -1
        if ball_x_pos - radius <= 0 or ball_x_pos + radius >= frame_width:
            ball_x_change *= -1
        if ball_y_change == 0:
            ball_y_change = 1
            ball_x_change = (ball_x_change / abs(ball_x_change)) * (math.sqrt(math.pow(ball_speed, 2) - math.pow(ball_x_change, 2)))
        ball_x_pos += int(ball_x_change)
        ball_y_pos += int(ball_y_change)

        # Draw Objects
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, deep_purple, [block_x_pos, block_y_pos, blockWidth,
                                                    blockHeight])
        pygame.draw.circle(gameDisplay, white, [ball_x_pos, ball_y_pos], radius)
        pygame.display.update()

        while gameOver == True:
            message_screen("Game Over, Press Space to Play Again or Q to Quit...", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        clock.tick(FPS)

    pygame.quit()
    quit()


gameLoop()
