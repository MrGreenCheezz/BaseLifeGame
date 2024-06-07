
import pygame
import random

pygame.init()
clock = pygame.time.Clock()

width, height = 900, 600
arrayWidth, arrayHeight = 300, 200

screen = pygame.display.set_mode((width, height))


CellsArray = [[0 for _ in range(arrayHeight)] for _ in range(arrayWidth)]

def PlaceCell(x, y):
    pygame.draw.rect(screen, (255, 255, 255), (x * 3, y * 3, 3, 3))

def CheckNeighbours(x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if x + i < 0 or x + i >= arrayWidth or y + j < 0 or y + j >= arrayHeight or (i == 0 and j == 0):
                continue
            elif CellsArray[x + i][y + j] == 1:
                count += 1
    return count

def GameTick():
    newCellsArray = [[CellsArray[x][y] for y in range(arrayHeight)] for x in range(arrayWidth)]
    for x in range(arrayWidth):
        for y in range(arrayHeight):
            count = CheckNeighbours(x, y)
            if CellsArray[x][y] == 1 and (count < 2 or count > 3):
                newCellsArray[x][y] = 0
            elif CellsArray[x][y] == 0 and count == 3:
                newCellsArray[x][y] = 1

    for x in range(arrayWidth):
        for y in range(arrayHeight):
            color = (255, 255, 255) if newCellsArray[x][y] == 1 else (0, 0, 0)
            pygame.draw.rect(screen, color, (x * 3, y * 3, 3, 3))
    
    return newCellsArray

def PlaceRandomCells():
    for i in range(arrayWidth):
        for j in range(arrayHeight):
            if random.random() < 0.7: 
                CellsArray[i][j] = 1


pygame.display.set_caption("Game of Life")


PlaceRandomCells()
CellsArray[10][10] = 1
CellsArray[11][10] = 1
CellsArray[12][10] = 1
CellsArray[12][9] = 1
CellsArray[11][8] = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    CellsArray = GameTick()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()