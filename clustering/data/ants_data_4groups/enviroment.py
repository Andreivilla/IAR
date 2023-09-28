#para fins de funcionalidade do programa 
#0 é um espaço vazio
#1 é um objeto (corpos de formigas
#-1 parede existe para definir os limites da proveta ou caso ela seja desenhada de alguma forma
import numpy as np
from ant import Ant
from random import uniform
from data import Data

class Enviroment:
    def __init__(self, enviorment=None):
        self.ants = []#vetor com formigas
        self.enviorment = enviorment#recebe um territorio pre definido ou chamar a funão generate_radom para criar 
        self.enviorment_ants = None#= self.ants_matrix()#gera o enviorment com a posição das formigas
        self.end = False

        self.col = len(self.enviorment)
        self.row = len(self.enviorment[0])

    #getters e setters necessarios 
    def get_row(self):
        return self.row
    def get_col(self):
        return self.col

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

    #atualiza as matrix de formigas
    def ants_matrix(self):
        #self.enviorment_ants = self.matrix_convert(self.enviorment)

        num_matrix = [['0'] * self.col for _ in range(self.row)]#cria uma matriz do tamanha da orginal só que apenas 0
        for i in range(self.row):
            for j in range(self.col):
                name = self.enviorment[i][j].name
                num_matrix[i][j] = name
        
        self.enviorment_ants = num_matrix

        #self.enviorment_ants = self.enviorment_ants.astype(object)
        for ant in self.ants:
            ant_position = ant.get_position()
            self.enviorment_ants[ant_position[0]][ant_position[1]] = ant.get_name()
        return self.enviorment_ants

    #funções de formiga        
    #nome para a nova formiga
    #posicao para a nova formiga um espaço aleatorio vazio(0)
        
    def choose_random_zero(self):
        while True:
            i = int(uniform(0, self.col))
            j = int(uniform(0, self.row))

            if int(self.enviorment[i][j].get_name()) == 0:
                
                return (i,j)        

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
    def get_ant_vision(self, ant, euclide=None):#(matrix, row, col, scalable_distance):
        ant_matrix = self.ants_matrix()
        rows = len(ant_matrix)
        cols = len(ant_matrix[0])
        #rows, cols = self.get_rowcol(self.ants_matrix())

        row, col = ant.get_position()
        ant_degree = ant.get_degree()
        vision = []

        for r in range(max(0, row - ant_degree), min(rows, row + ant_degree + 1)):
            for c in range(max(0, col - ant_degree), min(cols, col + ant_degree + 1)):
                if r == row and c == col:
                    continue
                if euclide == None:#para o calculo da matriz euclideana precisamos dos dados adjacentes que não são necessarios para se mover
                    vision.append((self.enviorment_ants[r][c], (r, c)))
                else:
                    vision.append((self.enviorment[r][c], (r, c)))

        return vision
    
    #atualizar formiga e lista de formigas
    def update_ant(self, ant):
        self.ants[ant.get_id] = ant
        self.ants_matrix()

    #funçoes para pegar e largar itens e calcular se deve fazer isso
    def get_enviroment_value(self, position):#retorna o valor da posição em que se encontra a formiga
        return self.enviorment[position[0]][position[1]]
    def take_enviroment_iten(self, position):#pegou o iten troca o iten da matriz por um data nulo
        self.enviorment[position[0]][position[1]] = Data(0)
    def drop_enviroment_iten(self, position, iten):
        self.enviorment[position[0]][position[1]] = iten#troca o iten do local pelo da formiga
    def get_rowcol(matriz):
        return len(matriz), len(matriz[0])
    
    #move formigas
    def mov_ants(self):
        for ant in self.ants:            
            ant_vision = self.get_ant_vision(ant)
            
            #decizão de take ou drop
            #identificar se o espaço ocupado pela formiga tem um iten para então ela decidir se solta ou pega
            ant.set_underiten(self.get_enviroment_value(ant.get_position()))
            ant_vision_data = self.get_ant_vision(ant, 1) #o 1 poderia ser qualquer valor
            
            if int(ant.get_underiten().get_name()) >= 1:#ponto com iten decidir se formiga pega ou não o iten
                if ant.take_iten(ant_vision_data):
                    self.take_enviroment_iten(ant.get_position())
            else:#ponto vazio decidir se a formiga deve largar algo
                iten_drop = ant.drop_iten(ant_vision_data)
                if iten_drop != False:
                    self.drop_enviroment_iten(ant.get_position(), iten_drop)

            ant.mov_ant(ant_vision)

            #variavel pra matar as formigas
            if self.end:
                if ant.iten_load == False:#formiga vazia morre

                    self.kill_ant(ant)

    def end_simulation(self):
        self.end = True    
    
    #isso pode ser inutil p krl
    def kill_ants(self):
        count = 0
        for ant in self.ants:
            count += 1
            if count == 48:
                break
            self.kill_ant(ant)




    def kill_ant(self, ant):
        self.ants.remove(ant)# pop(ant)#ant.get_id())
