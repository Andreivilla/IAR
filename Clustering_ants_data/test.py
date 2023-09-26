from read_data import Read_data
from data import Data
from enviroment import Enviroment

rd = Read_data('data.txt')
enviroment = Enviroment(rd.buil_matrix())

row = rd.row
col = rd.col

printar = enviroment.ants_matrix()
for i in range(row):
    for j in range(col):
        print(printar[i][j], end=" ")
    print()

enviroment.create_ants(50)#cria 50 formigas

printar = enviroment.ants_matrix()
for i in range(row):
    for j in range(col):
        print(printar[i][j], end=" ")
    print()

enviroment.mov_ants()

printar = enviroment.ants_matrix()
for i in range(row):
    for j in range(col):
        print(printar[i][j], end=" ")
    print()





def calculatingDensity(self, ant, paramRet):#paramRet
    """Calcula a densidade na vizinhança"""
    qtdItens = 0 
    distances =[]
    density = 0.0
    #contando dados na vizinhança
    for i in range(-ant.vision, ant.vision+1):
        for j in range(-ant.vision, ant.vision+1):
            if i == 0 and j == 0:
                continue
            row = ant.row + i
            col = ant.column + j   

            row %= self.dimension
            col %= self.dimension  
            if self.board[row][col].isData == True:
                qtdItens+= 1   
                distance = self.euclideanDistance(ant, self.board[row][col], paramRet)
                dissim = 1.0 - (distance/self.alpha)
                #print(dissim)
                if(dissim >= 0.0):
                    density += dissim
                distances.append(distance)
    #print(distances)
    if density <=0:
        return 0.0
    else:
        final_density = density / 9
        return final_density

def euclideanDistance(self, ant, item, td):#escolhe entre take e drop
    #formiga atual, item é o item adjacente 
    """Calcula a distância entre a formiga e o item"""
    ant_row, ant_col = ant.get_position()[0], ant.get_position()[1]
    if td == "t":#t de take
        #PEGAR
        dx = self.board[ant.row][ant.column].x - item.x
        dy = self.board[ant.row][ant.column].y - item.y
        return np.sqrt(dx**2 + dy**2)
    else:
        #largar
        dx = ant.payload.x - item.x
        dy = ant.payload.y - item.y
        return np.sqrt(dx**2 + dy**2)
#enviroment.mov_ants()

#for r in read:
#    print(r.name)

#for data in rd.data:
#    print(data)
