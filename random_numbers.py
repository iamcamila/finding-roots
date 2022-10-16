import numpy as np

def aleatorios(quantidade, inicial):
    population = []
    if inicial != 0:
        for i in range(quantidade):
            aleatorio = np.random.random()
            population.append(round(aleatorio*inicial, 4))
    else:
        for i in range(quantidade):
            aleatorio = np.random.random()
            population.append(aleatorio)
    population.append(round(inicial, 4))
    return population

# a = 5
# b = 2
# c = aleatorios(a, b)
# print(c)