from enviroment import Enviroment
import pygame
import numpy as np
from read_data import Read_data
from data import Data

#parameteros da simulação
#linha por coluna
#ROW, COL, DENSITY = 60, 60, 3#Numero de linhas da matriz, numero de colunas, densidade de itens
NUM_ANTS = 50
ITERACAO = 3000000
#relacionado com o tamanho do front
CELL_SIZE = 10

rd = Read_data('data.txt')
enviroment = Enviroment(rd.buil_matrix())
#enviroment = Enviroment()
#enviroment.generate_radom(ROW, COL, DENSITY)

#enviroment.create_ants(NUM_ANTS)
start = False

# Configurações da janela
ROW, COL = enviroment.get_row(), enviroment.get_col()
WIDTH, HEIGHT = (COL)*CELL_SIZE, (ROW)*CELL_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)

FPS = 60

# Cores
#rosa
PINK1 = (255, 0, 255)
PINK2 = (234, 77, 255)
PINK3 = (113, 0, 128)

RED1 = (255, 0, 0)
RED2 = (230, 69, 69)
RED3 = (97, 0, 0)

ORANGE1 = (255, 162, 0)
ORANGE2 = (230, 187, 69)
ORANGE3 = (97, 71, 0)

GREEN1 = (0, 255, 0)
GREEN2 = (69, 230, 69)
GREEN3 = (0, 97, 0)

BLUE1 = (0, 0, 255)
BLUE2 = (29, 29, 97)
BLUE3 = (0, 0, 97)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GOLDENROD = (218,165,32)
PINK = (255,0,255)
GREEN = (0,255,0)


# Inicializa o Pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Ants')

#para renderiza a matriz é preciso converter em seus nomes
def matrix_convert(matrix):
    row = len(matrix)
    col = len(matrix[0])
    num_matrix = [['0'] * col for _ in range(row)]#cria uma matriz do tamanha da orginal só que apenas 0
    for i in range(row):
        for j in range(col):
            name = matrix[i][j].name
            num_matrix[i][j] = name
    return num_matrix


# Função para renderizar a matriz numpy na janela
def render_matrix(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == '-1':
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == 'r':
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == 'b':
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '1':
                pygame.draw.rect(screen, RED1, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '2':
                pygame.draw.rect(screen, RED2, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '3':
                pygame.draw.rect(screen, RED3, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '4':
                pygame.draw.rect(screen, PINK1, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '5':
                pygame.draw.rect(screen, PINK2, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '6':
                pygame.draw.rect(screen, PINK3, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '7':
                pygame.draw.rect(screen, ORANGE1, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '8':
                pygame.draw.rect(screen, ORANGE2, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '9':
                pygame.draw.rect(screen, ORANGE3, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '10':
                pygame.draw.rect(screen, BLUE1, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '11':
                pygame.draw.rect(screen, BLUE2, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '12':
                pygame.draw.rect(screen, BLUE3, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '13':
                pygame.draw.rect(screen, GREEN1, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '14':
                pygame.draw.rect(screen, GREEN2, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y][x] == '15':
                pygame.draw.rect(screen, GREEN3, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Matriz numpy inicial (0s e 1s)
#matrix = np.random.randint(2, size=(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE))

matrix = enviroment.ants_matrix()

clock = pygame.time.Clock()

running = True
iteracao = -1

while running:

    if iteracao == ITERACAO:
        enviroment.end_simulation()
    iteracao+=1
    print(iteracao)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualize a matriz numpy com novos valores (por exemplo, aleatórios)
    enviroment.mov_ants()    
    matrix = enviroment.ants_matrix()

    # Limpe a tela
    screen.fill(WHITE)

    # Renderize a matriz na tela
    render_matrix(matrix)


    # Atualize a janela
    pygame.display.flip()

    if start:
        pass
    else:
        input('press enter to start')
        enviroment.create_ants(NUM_ANTS)
        start = True
    
    if len(enviroment.ants) == 0:
        input('Enter para terminar')
        break
    
    clock.tick(FPS)

    


# Encerre o Pygame
pygame.quit()
