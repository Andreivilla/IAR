import pygame
import numpy as np

# Configurações da janela
class Ant:
    def __init__(self, id, name, position, degree):
        self.WIDTH, self.HEIGHT = 800, 600
        self.WINDOW_SIZE = (self.WIDTH, self.HEIGHT)
        self.CELL_SIZE = 20
        self.FPS = 60
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)

        # Inicializa o Pygame
        self.pygame.init()

        # Cria a janela
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.pygame.display.set_caption('Matriz Numpy em Pygame')    






# Função para renderizar a matriz numpy na janela
def render_matrix(matrix):
    for y in range(matrix.shape[0]):
        for x in range(matrix.shape[1]):
            if matrix[y, x] == 1:
                pygame.draw.rect(screen, BLACK, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else:
                pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Matriz numpy inicial (0s e 1s)
matrix = np.random.randint(2, size=(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE))

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualize a matriz numpy com novos valores (por exemplo, aleatórios)
    matrix = np.random.randint(2, size=(HEIGHT // CELL_SIZE, WIDTH // CELL_SIZE))

    # Limpe a tela
    screen.fill(WHITE)

    # Renderize a matriz na tela
    render_matrix(matrix)

    # Atualize a janela
    pygame.display.flip()

    clock.tick(FPS)

# Encerre o Pygame
pygame.quit()