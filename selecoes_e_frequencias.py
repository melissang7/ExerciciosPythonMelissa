from asyncore import read
import pandas as pd

dados = pd.read_csv(r'C:\Users\aluno10\Documents\melissa\aula_01_modulo_03\aluguel.csv', sep = ';')

selecao1 = dados['Tipo'] == 'Apartamento'
print(selecao1)

n1 = dados[selecao1].shape[0]
print('Número de apartamentos:', n1)

selecao2 = (dados['Tipo'] == 'Casa') | (dados['Tipo'] == 'Condomínio') | (dados['Tipo'] == 'Casa de Vila')

n2 = dados[selecao2].shape[0]
print('Número de casas, Casa, Condomínio e Casa de Vila é: ', n2)


selecao3 = ((dados['Area'] >= 60) & (dados['Area'] <=100))
n3 = dados[selecao3].shape[0]
print('Terrenos com mais de 60 e menos de 100: ',n3)

selecao4 = ((dados['Quartos'] >= 4) & (dados['Valor'] <= 2000))
n4 = dados[selecao4].shape[0]
print('Questao 4: ',n4)
