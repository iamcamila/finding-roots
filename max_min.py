from asyncio.windows_events import NULL
from cmath import sin
import numpy as np
from itertools import product
import matplotlib.pyplot as plt

def MaxAndMin(func, deriv):
    # Setting minimal and maximal intervals
    # xmin, xmax = [float(x) for x in input("x mínimo e x máximo: ").split()]
    xmin, xmax = -5, 5

    resp = []
    ponto = ""

    # Creating range with step
    range = np.arange(xmin, xmax, 0.01)

    for i in range:
        i = round(i,2)
        if(deriv(i) == 0):
            ponto = i
        resp.append(func(i))



    if (ponto == ""):
        print("Não existe ponto de Máximo ou Mínimo no intervalo para a função")
    else:
        print("Ponto de Máximo ou Mínimo da função na coordenada ( "+ str(ponto)+" , "+str(func(ponto))+" )")
        cubica = np.vectorize(func)
        # derivada = np.vectorize(deriv)
        plt.plot(range, cubica(range), 'b', label="f(x) = x²")
        # plt.plot(range, derivada(range), 'r', label="f'(x) = 3x²")
        plt.plot(ponto, func(ponto), 'go', label="Ponto de máximo ou mínimo")
        plt.title("Gráfico da função ")
        plt.legend(loc="best")

    # Show graph of function with max/min point if necessary
    #     mostrar = input("Deseja visualizar o gráfico? [Y] Sim [N] Não \n")
    #     if mostrar == 'Y' or mostrar == 'y':
    #         plt.show()

        return ponto