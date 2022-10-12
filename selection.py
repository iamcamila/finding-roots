from operator import index

def selection (initialPopulation, vet_error):
    # selecionar os 4 valores da população com menores erros
    for i in range(len(vet_error)):
        vet_error[i] = abs(vet_error[i])


    res = []

    for i in range(4):
        min_error = min(vet_error)
        index_value = vet_error.index(min_error)
        res.append(initialPopulation[index_value])
        initialPopulation.pop(index_value)
        vet_error.pop(index_value)

    return res
