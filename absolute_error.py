# x = valor esperado
# y = vetor de valores
def erro (x, y):
    err = []
    for i in range(len(y)):
        err.append(abs(round(y[i]-x, 4)))

    return err
