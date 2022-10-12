from absolute_error import erro
from random_numbers import aleatorios
from conversion import tobinario, todecimal
from max_min import MaxAndMin
from selection import selection
import numpy as np

# funcSin = np.sin #sin(x)
# derivSin = np.cos
print('--------- Termos da Função -----------')
a, b, c, d = [int(x) for x in input("Entre com os valores de a, b, c e d, respectivamente: ").split()]

# print('\n-------------- Função ----------------')
func = np.poly1d([a, b, c, d])
print(func)
deriv = func.deriv()

# calculando o Max/Min local da função
ponto = MaxAndMin(func, deriv)

# criando população inicial aleatória
qtd = 5
if ponto == None:
    ponto = 0

initialPopulation = aleatorios(qtd, ponto)
# print(initialPopulation)

# calculando erro da primeira geração
x = 1
vet_error = erro(x, initialPopulation)

# selecionando os melhores indivíduos
best_parents = selection(initialPopulation, vet_error)
print(best_parents)

# converter decimais em binario
binary_parents = []
for value in best_parents:
    binary_parents.append(tobinario(value))
print('\n----------- População em Binário -------------')
print(binary_parents)

# populacao_decimal = []
# for value in populacao_binario:
#     populacao_decimal.append(todecimal(value))
# print('\n----------- População em Decimal -------------')
# print(populacao_decimal)
