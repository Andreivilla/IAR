from data import Data
from math import sqrt
from random import uniform

class Read_data:
    def __init__(self, name_data):
        self.name_data = name_data
        self.data = []

    def read(self):
        with open(self.name_data, 'r') as archive:
            lines = archive.readlines()
            for line in lines:
                line_plit = line.strip().split('\t')
                if len(line_plit) == 3:
                    name = line_plit[2]
                    x = float(line_plit[0].replace(',', '.'))
                    y = float(line_plit[1].replace(',', '.'))
                    self.data.append(Data(name, x, y))
    
    def buil_matrix(self, row=0, col=0):
        self.read() #lê o arquivo e salva as datas
        len_min = len(self.data)
        
        if row*col < len_min:
            row = col = int(sqrt(len_min)*2.2)

        #cria uma matriz sem nenhum item
        self.matriz = [[Data('0') for _ in range(col)] for _ in range(row)]

        
        #preenche com os elementos em ordem aleatoria
        
        cont = 0#variavel para calcular se todos os numero já foram inseridos
        while(cont<len_min):
            i = int(uniform(0, col))
            j = int(uniform(0, row))

            if int(self.matriz[i][j].get_name()) == 0:
                self.matriz[i][j] = self.data[cont]
                cont += 1        
        
        
        #cercar matriz com -1
        # Cria uma nova matriz com uma linha e coluna adicionais
        matriz_cercada = [[Data('-1') for _ in range(col + 2)]]  # Cria a primeira linha com objetos Data nomeados -1

        # Preenche as linhas internas da nova matriz
        for i in range(row):
            nova_linha = [Data('-1')]  # Cria a primeira célula da nova linha com objeto Data nomeado -1
            nova_linha.extend(self.matriz[i])  # Adiciona os elementos da matriz original
            nova_linha.append(Data('-1'))  # Adiciona a última célula da nova linha com objeto Data nomeado -1
            matriz_cercada.append(nova_linha)  # Adiciona a nova linha à matriz cercada

        # Cria a última linha com objetos Data nomeados -1
        matriz_cercada.append([Data('-1') for _ in range(col + 2)])

        self.matriz = matriz_cercada
        self.row = row+2
        self.col = row+2

        return self.matriz