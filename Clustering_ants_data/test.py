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







#enviroment.mov_ants()

#for r in read:
#    print(r.name)

#for data in rd.data:
#    print(data)
