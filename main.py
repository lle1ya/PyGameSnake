from ctypes.wintypes import SIZE

import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

pygame.display.set_caption('Змейка')

length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 4

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    sc.fill(pygame.Color('black'))

    # Рисование змейки и яблока
    [(pygame.draw.rect(sc, pygame.Color('green'), (i,j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    # Движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Поедание яблок
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        fps += 0.25

    # Проигрыш
    if x < 0 or 0 > RES - SIZE or y < 0 or y > RES - SIZE:
        break
    if len(snake) != len(set(snake)):
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Контроль
    key = pygame.key.get_pressed()
    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'S': False, 'A': True, 'D': True}
    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'S': True, 'A': True, 'D': True}
    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'S': True, 'A': True, 'D': False}
    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'S': True, 'A': False, 'D': True}