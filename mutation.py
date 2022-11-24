import random

def mutation (new_population):
    muteded_population = []
    for value in new_population:
        new_value = ''

        for bit in value:
            doesMutate = random.random()
            if doesMutate < 0.05:
                if bit == '0':
                    bit = '1'
                elif bit == '1':
                    bit = '0'
        
            new_value += bit

        muteded_population.append(new_value)

    return muteded_population