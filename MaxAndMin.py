from asyncio.windows_events import NULL
from cmath import sin
import numpy as np
from itertools import product
import matplotlib.pyplot as plt

# Setting minimal and maximal intervals
xmin = float(input("x mínimo: "))
xmax = float(input("x máximo: "))


# Setting function
func = np.poly1d([1, 0, 0, 0]) # x**3
funcSin = np.sin #sin(x)

# Calculating devivative
deriv = func.deriv()
derivSin = np.cos


resp = []
ponto = ""

respSin = []
pontoSin = ""

# Creating range with step
range = np.arange(xmin, xmax, 0.01)
rangeSin = np.arange(xmin*np.pi, xmax*np.pi, np.pi/16)

for i in range:
    i = round(i,2)
    if(deriv(i) == 0):
        ponto = i
    resp.append(func(i))


for i in rangeSin:
    i=round(i, 2)
    if(round(derivSin(i),2) == 0):
        pontoSin = i
    respSin.append(funcSin(i))


if (ponto == ""):
    print("Não existe ponto de Máximo ou Mínimo no intervalo para a função x³")
else:
    print("Ponto de Máximo ou Mínimo da função x³ = ", ponto)
    cubica = np.vectorize(func)
    derivada = np.vectorize(deriv)
    plt.plot(range, cubica(range), 'b', label="f(x) = x³")
    plt.plot(range, derivada(range), 'r', label="f'(x) = 3x²")
    plt.plot(ponto, func(ponto), 'go', label="Ponto de máximo ou mínimo")
    plt.title("Gráfico da função x³")
    plt.legend(loc="upper left")
    plt.show()

if (pontoSin == ""):
    print("Não existe ponto de Máximo ou Mínimo no intervalo para a função sin(x)")
else:
    print("Ponto de Máximo ou Mínimo da função sin(x)= ", pontoSin)
    Sin = np.vectorize(funcSin)
    derivadaSin = np.vectorize(derivSin)
    plt.plot(rangeSin, derivadaSin(rangeSin), 'r', label="f'(x) = cos(x)")
    plt.plot(rangeSin, Sin(rangeSin),'b', label="f(x) = sin(x)")
    plt.plot(pontoSin, funcSin(pontoSin), 'go', label="Ponto de máximo ou mínimo")
    plt.title("Gráfico da função sin(x)")
    plt.legend(loc="upper left")
    plt.show()