#para fins de funcionalidade do programa 
#0 é um espaço vazio
#1 é um objeto (corpos de formigas
#-1 parede existe para definir os limites da proveta ou caso ela seja desenhada de alguma forma
import numpy as np
from ant import Ant

class Enviroment:
    def __init__(self, enviorment=None):
        self.ants = []#vetor com formigas
        self.enviorment = enviorment#recebe um territorio pre definido ou chamar a funão generate_radom para criar 
        self.enviorment_ants = None#= self.ants_matrix()#gera o enviorment com a posição das formigas
        self.end = False

    #atualiza as matrix de formigas
    def ants_matrix(self):
        self.enviorment_ants = self.enviorment
        self.enviorment_ants = self.enviorment_ants.astype(object)
        for ant in self.ants:
            ant_position = ant.get_position()
            self.enviorment_ants[ant_position[0], ant_position[1]] = ant.get_name()
        return self.enviorment_ants

    def get_ants_matrix(self):
        return self.enviorment_ants

    #gera matriz e cerca ela
    def generate_radom(self, row, col, density=1):
        # Gerar uma matriz aleatória de valores entre 0 e 1
        random_matrix = np.random.rand(row, col)
        # Converter os valores em binários (0 ou 1)
        binary_matrix = (random_matrix < (0.1*density)).astype(int)
        
        self.enviorment = binary_matrix.astype(object)
        #gera paredes ao redor de toda a matriz
        self.surround_enviorment()
        
    def surround_enviorment(self):
        linhas, colunas = self.enviorment.shape
        new_mat = np.ones((linhas + 2, colunas + 2)) * -1
        new_mat[1:-1, 1:-1] = self.enviorment
        self.enviorment = new_mat

    #funções de formiga        
    #nome para a nova formiga
    #posicao para a nova formiga um espaço aleatorio vazio(0)
    def choose_random_zero(self):
        zero_positions = np.argwhere(self.ants_matrix() == 0)
        
        if len(zero_positions) == 0:#não deve acontecer mas caso não exista mais zeros na matriz
            #print(self.enviorment)
            raise ValueError("A matriz não possui espaço para uma nova formiga")
        
        random_zero_position = zero_positions[np.random.randint(len(zero_positions))]
        return tuple(random_zero_position)

    def add_new_ant(self, vison_degree):#vision_degree cria o nivel de visão da formiga
        if len(self.ants) == 0:
            new_ant = Ant(0, 'b', self.choose_random_zero(), vison_degree)
        else:
            new_ant = Ant(self.ants[-1].get_id()+1, 'b', self.choose_random_zero(), vison_degree)    

        self.ants.append(new_ant)

    def create_ants(self, num, degree = 1):
        for i in range(num):
            self.add_new_ant(degree)

        
    #funçao para indicar a area de visão para a formiga
    def get_ant_vision(self, ant):#(matrix, row, col, scalable_distance):
        #print(self.ants_matrix().shape())
        rows, cols = self.ants_matrix().shape
        row, col = ant.get_position()
        ant_degree = ant.get_degree()
        vision = []

        for r in range(max(0, row - ant_degree), min(rows, row + ant_degree + 1)):
            for c in range(max(0, col - ant_degree), min(cols, col + ant_degree + 1)):
                if r == row and c == col:
                    continue
                vision.append((self.enviorment_ants[r, c], (r, c)))

        return vision
    
    #atualizar formiga e lista de formigas
    def update_ant(self, ant):
        self.ants[ant.get_id] = ant
        self.ants_matrix()

    #funçoes para pegar e largar itens e calcular se deve fazer isso
    def get_enviroment_value(self, position):#retorna o valor da posição em que se encontra a formiga
        return self.enviorment[position[0], position[1]]
    def take_enviroment_iten(self, position):
        self.enviorment[position[0], position[1]] = 0
    def drop_enviroment_iten(self, position):
        self.enviorment[position[0], position[1]] = 1

    #move formigas
    def mov_ants(self):
        for ant in self.ants:            
            ant_vision = self.get_ant_vision(ant)
            #identificar se o espaço ocupado pela formiga tem um iten para então ela decidir se solta ou pega
            point_value = self.get_enviroment_value(ant.get_position())

            if point_value == 1:#ponto com iten decidir se formiga pega ou não o iten
                if ant.take_iten(ant_vision):
                    self.take_enviroment_iten(ant.get_position())
            else:#ponto ocupado decidir se a formiga deve pegar algo
                if ant.drop_iten(ant_vision):
                    self.drop_enviroment_iten(ant.get_position())

            ant.mov_ant(ant_vision)

            #variavel pra matar as formigas
            if self.end:
                if ant.get_iten() == False:#formiga vazia morre
                    self.kill_ant(ant)

    def end_simulation(self):
        self.end = True
    
    
    #isso pode ser inutil p krl
    def kill_ants(self):
        count = 0
        for ant in self.ants:
            count += 1
            print(count)
            if count == 48:
                print('break matança')
                break
            self.kill_ant(ant)
            print( 'depois do ant')




    def kill_ant(self, ant):
        self.ants.remove(ant)# pop(ant)#ant.get_id())
            
    





            



