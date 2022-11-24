import time
from matplotlib import pyplot as plt
from absolute_error import erro
from crossover import crossover
from mutation import mutation
from random_numbers import aleatorios
from conversion import tobinario, todecimal
from max_min import MaxAndMin
from selection import selection
import numpy as np
import pandas as pd

# Start stopwatch
inicio = time.time()

# Function terms
# a, b, c, d = [int(x) for x in input("Entre com os valores de a, b, c e d, respectivamente: ").split()]
# func = np.poly1d([a, b, c, d])
func = np.poly1d([1, 1, 1, 1, -4])
print(func)
deriv = func.deriv()

# Max/Min calculation
ponto = MaxAndMin(func, deriv)

graf = []
melhor_valor = []
iteracao = []

# Setting counter for multiple runs
for contador in range(100):
    # defining quantity of desired inicial population minus 1 (that comes from max/min point).
    qtd = 999
    
    # defining default value of max/min point
    if ponto == None:
        ponto = 0

    # creating initial population
    initialPopulation = aleatorios(qtd, ponto)

    # defining wated value
    x = -1.6506
    
    iteration = 0
    min_error = 1

    while  min_error > 0.001: # wanted min_error
        if iteration == 1000: # wated max iteration
            break

        iteration+=1

        # Evaluation - absolute error calculation
        vet_error = erro(x, initialPopulation)

        # Selection - selecting the best individuals
        best_parents = selection(initialPopulation, vet_error)

        # setting best individual graph
        graf.append(best_parents[0])

        # Converting decimals to binary
        binary_parents = []
        for value in best_parents:
            binary_parents.append(tobinario(value))

        # Reproduction - crossing pair by pair
        new_parents = crossover(binary_parents)

        # Mutation - randomly mutate genes of individuals
        new_parents = mutation(new_parents)

        # converting binary to decimal
        new_population_decimal = []
        for value in new_parents:
            new_population_decimal.append(todecimal(value))

        # New population
        initialPopulation = new_population_decimal
        
        vet_error = erro(x, initialPopulation)
        min_error = min(vet_error)

        closer = 100
        for value in initialPopulation:
            if closer > abs(x-value):
                closest = value
                closer = abs(x-value)


    melhor_valor.append(closest)
    iteracao.append(iteration)
    graf.append(closest)
    
    # To plot graph if needed
    # graf_error = erro(x, graf)
    # range = np.arange(0, iteration+1, 1)
    # plt.plot(range, graf_error, 'bP')
    # plt.axhline(y=0)
    # plt.show()
    contador+=1

# Creating data set to export
mv = []
for number in melhor_valor:
    mv.append(str(number).replace(".", ","))

data = zip(iteracao,mv)
data_df = pd.DataFrame(data)
print(data)
print(data_df)

data_it = pd.DataFrame(iteracao)
data_mv = pd.DataFrame(mv)

data_df.to_csv("results.csv", index = False, header = False)
data_it.to_csv("iteration.csv", index = False, header = False)
data_mv.to_csv("best value.csv", index = False, header = False)

# Stop stopwatch
fim = time.time()

# Time spent
print(fim - inicio)