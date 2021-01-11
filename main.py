import sys
import time

from hfun import *

pygame.init()

grid = [[0 for i in range(9)] for j in range(9)]
engaged = False
pygame.display.set_caption('SUDOKU SOLVER')

surface = pygame.display.set_mode((WIDTH, WIDTH))


def solve():
    global grid
    for i in range(9):
        time.sleep(0.01)  # to make it look cool !
        for j in range(9):

            if grid[i][j] == 0:
                for n in range(1, 10):
                    if verify(i, j, n, grid):
                        grid[i][j] = n

                        if n == 1:
                            surface.blit(ONE, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 2:
                            surface.blit(TWO, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 3:
                            surface.blit(THREE, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 4:
                            surface.blit(FOUR, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 5:
                            surface.blit(FIVE, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 6:
                            surface.blit(SIX, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 7:
                            surface.blit(SEVEN, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 8:
                            surface.blit(EIGHT, (i * rect_width + 2, j * rect_width + 2))
                        elif n == 9:
                            surface.blit(NINE, (i * rect_width + 2, j * rect_width + 2))
                        pygame.display.update()
                        solve()
                        grid[i][j] = 0
                        pygame.draw.rect(surface, WHITE,
                                         [i * rect_width + 2, j * rect_width + 2, rect_width - 2, rect_width - 2])
                return
    pygame.display.set_caption('SOLVED')
    while True:
        for event1 in pygame.event.get():
            if event1.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)


def set_stage():
    surface.fill(WHITE)
    for i in range(9):
        if i % 3 == 0:
            pygame.draw.line(surface, BLACK, (0, rect_width * i), (WIDTH, rect_width * i), 3)
            pygame.draw.line(surface, BLACK, (rect_width * i, 0), (rect_width * i, WIDTH), 3)
        else:
            pygame.draw.line(surface, BLACK, (0, rect_width * i), (WIDTH, rect_width * i))
            pygame.draw.line(surface, BLACK, (rect_width * i, 0), (rect_width * i, WIDTH))
    pygame.display.update()


set_stage()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not engaged:
                engaged = True
                rec_pos = get_tile(pygame.mouse.get_pos())
            else:
                engaged = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.display.set_caption('SOLVING...')
                solve()
            if engaged:
                number = 0
                if event.key == pygame.K_0:
                    # noinspection PyUnboundLocalVariable
                    pygame.draw.rect(surface, WHITE, [rec_pos[0] + 2, rec_pos[1] + 2, rect_width - 2, rect_width - 2])
                    number = 0
                elif event.key == pygame.K_1:
                    surface.blit(ONE, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 1
                elif event.key == pygame.K_2:
                    surface.blit(TWO, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 2
                elif event.key == pygame.K_3:
                    surface.blit(THREE, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 3
                elif event.key == pygame.K_4:
                    surface.blit(FOUR, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 4
                elif event.key == pygame.K_5:
                    surface.blit(FIVE, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 5
                elif event.key == pygame.K_6:
                    surface.blit(SIX, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 6
                elif event.key == pygame.K_7:
                    surface.blit(SEVEN, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 7
                elif event.key == pygame.K_8:
                    surface.blit(EIGHT, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 8
                elif event.key == pygame.K_9:
                    surface.blit(NINE, (rec_pos[0] + 2, rec_pos[1] + 2))
                    number = 9
                grid[int(rec_pos[0] / rect_width)][int(rec_pos[1] / rect_width)] = number
                pygame.display.update()
