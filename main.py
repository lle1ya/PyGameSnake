import pygame

BackColor = (188, 143, 143)
Wsite = (255, 235, 205)
Gsite = (192, 192, 192)

size = [590, 600]
SIZE_BLOCK = 20
COUNT_BLOCKS = 27
Margin = 1

screen = pygame.display.set_mode(size)
pygame.display.set_caption('Змейка')

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill(BackColor)

    for row in range(COUNT_BLOCKS):
        for column in range(COUNT_BLOCKS):
            if (row + column) % 2 == 0:
                color = Wsite
            else:
                color = Gsite
            pygame.draw.rect(screen,color, [10 + column * SIZE_BLOCK + Margin*(column+1),
                                                 20 + row * SIZE_BLOCK + Margin*(row+1),SIZE_BLOCK,SIZE_BLOCK])

    pygame.display.flip()