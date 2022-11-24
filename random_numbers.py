import numpy as np

def aleatorios(quantidade, inicial):
    population = []
    if inicial != 0:
        for i in range(quantidade):
            aleatorio = np.random.random()*10
            population.append(round(aleatorio*inicial, 4))
    else:
        for i in range(quantidade):
            aleatorio = np.random.random()*10
            population.append(round(aleatorio, 4))
    population.append(round(inicial, 4))
    return population
