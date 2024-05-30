import pygame
import sys
from random import randrange

# Инициализация Pygame
pygame.init()

# Установка размеров экрана
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Змейка')

# Цвета
white = (255, 255, 255)
black = (0, 0, 0)

# Основной цикл игры
def main_menu():
    menu = True
    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(white)
        # Отображение текста меню
        font = pygame.font.SysFont(None, 75)
        text = font.render("Змейка", True, black)
        screen.blit(text, (screen_width/2 - text.get_width()/2, screen_height/3))

        # Создание кнопок меню
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Рисование прямоугольников для кнопок
        if 150+100 > mouse[0] > 150 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, black,(165,450,90,50))
            if click[0] == 1:
                menu = False
        else:
            pygame.draw.rect(screen, white,(150,450,100,50))

        if 550+100 > mouse[0] > 550 and 450+50 > mouse[1] > 450:
            pygame.draw.rect(screen, black,(565,450,90,50))
            if click[0] == 1:
                pygame.quit()
                sys.exit()
        else:
            pygame.draw.rect(screen, white,(550,450,100,50))

        # Отображение текста на кнопках
        small_font = pygame.font.SysFont(None, 35)
        text_start = small_font.render("Начать", True, black)
        text_quit = small_font.render("Выход", True, black)
        screen.blit(text_start, (150+20,450+10))
        screen.blit(text_quit, (550+20,450+10))

        pygame.display.update()

main_menu()

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'S': True, 'A': True, 'D': True}

length = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 4

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Arial', 26, bold=True)
font_fps = pygame.font.SysFont('Arial', 26, bold=True)
font_end = pygame.font.SysFont('Arial', 66, bold=True)

while True:
    sc.fill(pygame.Color('black'))

    # Рисование змейки и яблока
    [(pygame.draw.rect(sc, pygame.Color('green'), (i,j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    #Очки и скорость
    render_score = font_score.render(f'ОЧКИ: {score}', 1, pygame.Color('orange'))
    sc.blit(render_score, (5, 5))
    render_fps = font_fps.render(f'СКОРОСТЬ: {fps}', 1, pygame.Color('green'))
    sc.blit(render_fps, (580, 5))

    # Движение змейки
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    # Поедание яблок
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 100
        fps += 0.5

    # Проигрыш
    if (x < 0 or x > RES - SIZE) or (y < 0 or y > RES - SIZE) or (len(snake) != len(set(snake))):
        while True:
            render_end = font_end.render('КОНЕЦ ИГРЫ', 1, pygame.Color('orange'))
            sc.blit(render_end, (RES // 2 - 200, RES // 3))
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

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