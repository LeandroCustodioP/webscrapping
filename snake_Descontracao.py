import pygame, random
from pygame.locals import *

UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake')

snake = [(200,200),(210,200),(220,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((255,255,255))

apple_pos = (random.randint(0,590),random.randint(0,590))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))

my_direction = pygame.LEFT

clock = pygame.time.Clock()

while True:
    clock.tick(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.k_UP:
                my_direction = UP 
            if event.key == pygame.k_RIGHT:
                my_direction = RIGHT 
            if event.key == pygame.k_DOWN:
                my_direction = DOWN
            if event.key == pygame.k_LEFT:
                my_direction = LEFT  

    if my_direction == pygame.UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if my_direction == pygame.RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == pygame.DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    if my_direction == pygame.LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])

    for i in range(len(snake) -1,0,-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    screen.fill((0,0,0))
    screen.blit(apple,apple_pos)
    for pos in snake:
        screen.blit(snake_skin,pos)

    pygame.display.update()