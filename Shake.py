import pygame
from random import randrange

RES = 800
SIZE = 50

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5


pygame.init()
screen = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()

while True:
    screen.fill(pygame.Color('black'))
    [(pygame.draw.rect(screen, pygame.Color('green'), (i, j, SIZE, SIZE))) for i, j in snake]
    pygame.draw.rect(screen, pygame.Color('red'), (*apple, SIZE, SIZE))
    font_socre = pygame.font.SysFont('Arial', 26, bold=True)
    render_score = font_socre.render(f'SCORE: {lenght}', 1, pygame.Color('pink'))
    screen.blit(render_score, (5, 5))
    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-lenght:]
    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        lenght += 1
        fps += 1
    if x > 800 or x < 0 or y > 800 or y < 0:
        break
    if len(snake) != len(set(snake)):
        break
    pygame.display.flip()
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # Control
    knopka = pygame.key.get_pressed()
    if knopka[pygame.K_w]:
        dx, dy = 0, -1
    if knopka[pygame.K_s]:
        dx, dy = 0,  1
    if knopka[pygame.K_d]:
        dx, dy = 1, 0
    if knopka[pygame.K_a]:
        dx, dy = -1, 0