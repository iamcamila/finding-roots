import numpy as np

def aleatorios(quantidade, inicial):
    population = []
    if inicial != 0:
        for i in range(quantidade):
            aleatorio = np.random.random()
            population.append(aleatorio*inicial)
    else:
        for i in range(quantidade):
            aleatorio = np.random.random()
            population.append(aleatorio)
    population.append(inicial)
    return population