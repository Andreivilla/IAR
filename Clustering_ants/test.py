import numpy as np

def generate_radom(row, col, density=1):
    # Gerar uma matriz aleatória de valores entre 0 e 1
    random_matrix = np.random.rand(row, col)
    # Converter os valores em binários (0 ou 1)
    print(random_matrix)
    binary_matrix = (random_matrix < 0.5).astype(int)
    
    enviorment = binary_matrix.astype(object)

    return enviorment

matriz = generate_radom(30, 30)
print(matriz)

#tem que fazer o drop ser mais interessandte perto dos bagulho
# e o take a mais interessante onde tiver mais vazio
#a matriz sem formigas é o resultado da simulação
#então deixa os cara carregado trabalhar até o final e retorna só a matriz final
#melhorar logica de deslocamento por exemplo formiga descarregada com mais vontade de ir pra lugar carregado
#formiga carregada com mais votade por lugar branco
#formiga que não volta