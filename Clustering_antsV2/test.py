#tem que fazer o drop ser mais interessandte perto dos bagulho
# e o take a mais interessante onde tiver mais vazio
#a matriz sem formigas é o resultado da simulação
#então deixa os cara carregado trabalhar até o final e retorna só a matriz final
#melhorar logica de deslocamento por exemplo formiga descarregada com mais vontade de ir pra lugar carregado
#formiga carregada com mais votade por lugar branco
#formiga que não volta

from read_data import Read_data
from data import Data

rd = Read_data('data.txt')

rd.read()

read = rd.data

#for r in read:
#    print(r.name)

print(rd.d)
