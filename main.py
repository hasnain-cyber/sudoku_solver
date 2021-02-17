import sys

from hfun import *

pygame.init()
pygame.display.set_caption('SUDOKU SOLVER')
surface = pygame.display.set_mode((WIDTH, WIDTH))

grid = [[0 for i in range(9)] for j in range(9)]
recPos = (0, 0)


def solve():
    global grid
    for i in range(9):
        # time.sleep(0.01)  # to make it look cool !
        for j in range(9):

            if grid[i][j] == 0:
                for n in range(1, 10):
                    if verify(i, j, n, grid):
                        grid[i][j] = n

                        if n == 1:
                            surface.blit(ONE, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 2:
                            surface.blit(TWO, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 3:
                            surface.blit(THREE, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 4:
                            surface.blit(FOUR, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 5:
                            surface.blit(FIVE, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 6:
                            surface.blit(SIX, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 7:
                            surface.blit(SEVEN, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 8:
                            surface.blit(EIGHT, (j * rect_width + 2, i * rect_width + 2))
                        elif n == 9:
                            surface.blit(NINE, (j * rect_width + 2, i * rect_width + 2))
                        pygame.display.update()

                        solve()
                        grid[i][j] = 0
                        pygame.draw.rect(surface, WHITE,
                                         [j * rect_width + 2, i * rect_width + 2, rect_width - 2, rect_width - 2])
                return
    pygame.display.set_caption('SOLVED')
    print(grid)
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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            recPos = get_tile(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            number = 0
            if event.key == pygame.K_0:
                pygame.draw.rect(surface, WHITE, [recPos[0] + 2, recPos[1] + 2, rect_width - 2, rect_width - 2])
                number = 0
            elif event.key == pygame.K_1:
                surface.blit(ONE, (recPos[0] + 2, recPos[1] + 2))
                number = 1
            elif event.key == pygame.K_2:
                surface.blit(TWO, (recPos[0] + 2, recPos[1] + 2))
                number = 2
            elif event.key == pygame.K_3:
                surface.blit(THREE, (recPos[0] + 2, recPos[1] + 2))
                number = 3
            elif event.key == pygame.K_4:
                surface.blit(FOUR, (recPos[0] + 2, recPos[1] + 2))
                number = 4
            elif event.key == pygame.K_5:
                surface.blit(FIVE, (recPos[0] + 2, recPos[1] + 2))
                number = 5
            elif event.key == pygame.K_6:
                surface.blit(SIX, (recPos[0] + 2, recPos[1] + 2))
                number = 6
            elif event.key == pygame.K_7:
                surface.blit(SEVEN, (recPos[0] + 2, recPos[1] + 2))
                number = 7
            elif event.key == pygame.K_8:
                surface.blit(EIGHT, (recPos[0] + 2, recPos[1] + 2))
                number = 8
            elif event.key == pygame.K_9:
                surface.blit(NINE, (recPos[0] + 2, recPos[1] + 2))
                number = 9
            grid[int(recPos[1] / rect_width)][int(recPos[0] / rect_width)] = number
            pygame.display.update()

            if event.key == pygame.K_SPACE:
                pygame.display.set_caption('SOLVING...')
                solve()
