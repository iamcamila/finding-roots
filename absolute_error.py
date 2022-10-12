# x = valor esperado
# y = vetor de valores
def erro (x, y):
    err = []
    for i in range(len(y)):
        # err.append(round(y[i]-x, 3))
        err.append(y[i]-x)
    return err
