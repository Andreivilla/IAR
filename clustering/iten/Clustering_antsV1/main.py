from enviroment import Enviroment
import pygame
import numpy as np

#parameteros da simulação
#linha por coluna
ROW, COL, DENSITY = 60, 60, 3#Numero de linhas da matriz, numero de colunas, densidade de itens
NUM_ANTS = 50
ITENRACAO = 1200000
#relacionado com o tamanho do front
CELL_SIZE = 10

enviroment = Enviroment()
enviroment.generate_radom(ROW, COL, DENSITY)

#enviroment.create_ants(NUM_ANTS)
start = False

# Configurações da janela

WIDTH, HEIGHT = (COL+2)*CELL_SIZE, (ROW+2)*CELL_SIZE
WINDOW_SIZE = (WIDTH, HEIGHT)

FPS = 60

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Inicializa o Pygame
pygame.init()

# Cria a janela
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption('Ants')

# Função para renderizar a matriz numpy na janela
def render_matrix(matrix):
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            if matrix[y, x] == 1 or matrix[y, x] == -1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y, x] == 'r':
                pygame.draw.rect(screen, RED, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            elif matrix[y, x] == 'b':
                pygame.draw.rect(screen, BLUE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Matriz numpy inicial (0s e 1s)
#matrix = np.random.randint(2, size=(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE))

matrix = enviroment.ants_matrix()

clock = pygame.time.Clock()

running = True
iteracao = -1
while running:


    if iteracao == ITENRACAO:
        enviroment.end_simulation()
    iteracao+=1
    print(iteracao)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualize a matriz numpy com novos valores (por exemplo, aleatórios)
    enviroment.mov_ants()    
    matrix = enviroment.ants_matrix()
    #print(enviroment.ants_matrix())

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
