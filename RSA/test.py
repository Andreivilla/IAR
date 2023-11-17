import numpy as np
#from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
#breast_cancer_wisconsin_original = fetch_ucirepo(id=15) 
  
# data (as pandas dataframes) 
#X = breast_cancer_wisconsin_original.data.features 
#y = breast_cancer_wisconsin_original.data.targets 

# metadata 
#print(breast_cancer_wisconsin_original.metadata) 
  
# variable information 
#print(breast_cancer_wisconsin_original.variables) 

def extract_data(arq):
    lines = []

    with open(arq, 'r') as file:
        for line in file:
            values = line.strip().split(',')

            #elimina linhas com ?
            if '?' not in values:
                lines.append(values)

    return np.array(lines)#.astype(float)

def normalize(arq):
    data = extract_data(arq)
    norm = np.linalg.norm(data, axis=1, keepdims=True)
    print(data/norm)
    #return data / norm
def normalizar_linhas(matriz):
    
    # Calcular a norma (magnitude) de cada linha
    normas_linhas = np.linalg.norm(matriz, axis=1, keepdims=True)

    # Normalizar cada linha dividindo pelos seus respectivos valores de norma
    matriz_normalizada = matriz / normas_linhas

    return matriz_normalizada
# Exemplo de uso:
#arq = "data/breast-cancer-wisconsin.data"
#arq = "data/wdbc.data"
#arq = "data/wpbc.data"
#print(extract_data(arq))

#breast_cancer = extract_data("data/breast-cancer-wisconsin.data")
#wdbc = extract_data("data/wdbc.data")
#wpbc = extract_data("data/wpbc.data")

#normalize("data/breast-cancer-wisconsin.data")
normalizar_linhas(extract_data("data/breast-cancer-wisconsin.data"))
#print(wdbc)
#print(wpbc)
#função para normalizar dataset
def normalize(X, min_val=-1, max_val=1):
    # Substituir NaN por zero
    X[np.isnan(X)] = 0

    # Normalizar X entre min_val e max_val
    X_normalized = min_val + 2 * (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0)) * (max_val - min_val)

    return X_normalized