import random
import numpy as np

class Ant:
    def __init__(self, id, name, position, degree):
        self.id = id
        self.name = name#nome para exibição apenas
        self.position = position #(i,j)
        self.iten = False
        self.vision_degree = degree 
    
    #funções para pegar valores do objeto
    def get_name(self):
        return self.name
    
    def get_position(self):
        return self.position

    def get_degree(self):
        return self.vision_degree
    
    def get_id(self):
        return self.id
    
    def get_iten(self):
        return self.iten
        
    
    #mov_ant deve receber a visão do ambiente com base em seu grau de visão e retornar um movimento valido    
    def mov_ant(self, vision):
        adjacent_values = []
        row, col = self.get_position()
        #armazena todos os valores adjacentes onde a formiga pode se mover
        for value, point in vision:
            if point[0] == row or point[1] == col:
                if value == 0 or value == 1:#a formiga só pode andar pra 0 ou 1 nunca -1 ou outra formiga x
                    adjacent_values.append((value, point))
        
        if len(adjacent_values) != 0:
            move_position = random.choice(adjacent_values)[1]
            self.position = move_position
     
    
    def chance(self, vision):
        Qi, Qcel = 0, 0
        for value, point in vision:
            Qcel+=1

            if value == 1:
                Qi+=1

        return Qi/Qcel
    
    def chance_choice(self, chance):
        #if random.random() <= chance:
        if np.random.rand() <= chance:
            return True
        else:
            False

    #funções de drop e take
    #drop e take servem para modificar o nome e o estado da formiga
    #criadas apenas pra simplicar e deixar o print mais elegante
    def take(self):
        self.iten = True
        self.name = 'r'#r = red descarregada
    def drop(self):
        self.iten = False
        self.name = 'd'#b = blue carredaga

    def take_iten(self, vision):
        #se a formiga esta descarregada ela pode pegar um iten
        if self.iten: #a formiga possui um iten 
            return False#já possui um iten não pode carregar mais
        else:#não possui um iten podemos decidir se carrega algo
            chance = 1-self.chance(vision)

            if chance == 0:#se a chance for zero não pega os itens
                return False

            if self.chance_choice(chance):#sorteia uma chance
                    self.take()
                    #self.iten = True#pega iten
                    return True#retorna o comando de pegar para a matriz
            
            else:#não tem nada  a pegar
                return False

    def drop_iten(self, vision):
        if self.iten:#a formiga esta carregada pode largar um iten
            chance = self.chance(vision)

            if chance == 1:#se for um esta cercada e descarrega o iten
                self.iten = False
                return True

            #sorteia a chance e altera se esta descarregada
            if self.chance_choice(chance):
                self.drop()
                #self.iten = False
                return True

            else:#ponto cheio não pode descarregar nada aqui
                return False
