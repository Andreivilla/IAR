import random
import numpy as np

class Ant:
    def __init__(self, id, name, position, degree):
        self.id = id
        self.name = name#nome para exibição apenas
        self.position = position #(i,j)
        self.iten_load = False
        self.iten = None
        self.vision_degree = degree 

        self.k1 = 0.1
        self.k2 = 0.3
        self.alpha = 20
    
    #funções para pegar valores do objeto
    '''
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
    '''
    def set_underiten(self, iten):
        self.under_iten = iten
    def get_underiten(self):
        return self.under_iten
    
    #mov_ant deve receber a visão do ambiente com base em seu grau de visão e retornar um movimento valido    
    def mov_ant(self, vision):
        adjacent_values = []
        row, col = self.position

        #armazena todos os valores adjacentes onde a formiga pode se mover
        for value, point in vision:
            if point[0] == row or point[1] == col:
                if value == 'r' or value == 'd' or value == 'b':
                    continue
                elif int(value) >= 0:#a formiga só pode andar pra 0 ou 1 nunca -1 ou outra formiga x
                    adjacent_values.append((value, point))

        if len(adjacent_values) != 0:
            move_position = random.choice(adjacent_values)[1]
            self.position = move_position

    #densidade e distancia
    def euclideanDistance(self, iten):#escolhe entre take e drop
        #formiga atual, item é o item adjacente 
        """Calcula a distância entre a formiga e o item"""
        if self.iten_load:#isso aqui vai ser dentro da formiga el apode ver só se ta carregado ou não
            #largar
            dx = self.iten.x - iten.x
            dy = self.iten.y - iten.y
            return np.sqrt(dx**2 + dy**2)
        else:
            #PEGAR
            #iten que a formiga ta em cima
            dx = self.under_iten.x - iten.x
            dy = self.under_iten.y - iten.y
            return np.sqrt(dx**2 + dy**2)


    def calculatingDensity(self, vision):
        """Calcula a densidade na vizinhança"""
        qtdItens = 0 
        distances =[]
        density = 0.0

        for itentuple in vision:
            iten = itentuple[0]
            if int(iten.name) > 0:
                qtdItens+=1
                distance = self.euclideanDistance(iten)
                dissim = 1.0 - (distance/self.alpha)
                
                if(dissim >= 0.0):
                    density += dissim
                distances.append(distance)

        if density <=0:
            return 0.0
        else:
            final_density = density / 9
            return final_density
    
    #funções de drop e take
    #drop e take servem para modificar o nome e o estado da formiga
    #criadas apenas pra simplicar e deixar o print mais elegante
    def take(self):
        self.iten = self.under_iten
        self.under_iten = None
        self.iten_load = True
        self.name = 'r'#r = red descarregada
    def drop(self):
        iten_drop = self.iten
        self.iten = None
        self.iten_load = False
        self.name = 'd'#b = blue carredaga
        return iten_drop

    def take_iten(self, vision):
        #se a formiga esta descarregada ela pode pegar um iten
        if self.iten_load: #a formiga possui um iten
            return False#já possui um iten não pode carregar mais
        else:#não possui um iten podemos decidir se carrega algo
            randPegar = np.random.rand()#gera um numero aleatorio
            density = self.calculatingDensity(vision)
            coeff = (self.k1 / (self.k1 + density))**2
            if(randPegar < coeff ):
                self.take()
                return True            
            else:#não pega pela chance
                return False

    def drop_iten(self, vision):
        if self.iten_load:#a formiga esta carregada pode largar um iten
            randLargar = np.random.rand()
            density = self.calculatingDensity(vision)
            coeff = (density / (self.k2 + density))**2

            if(randLargar < coeff):
                iten = self.drop()
                return iten
            else:#não larga pela chance
                return False
        else:#ponto cheio não pode descarregar nada aqui
            return False

