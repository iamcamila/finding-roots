
def crossover (binary_parents):
    new_population = []

    while len(binary_parents) != 0:
        parent1  = binary_parents[0].split('.')
        parent2 = binary_parents[1].split('.')

        #sinal
        sinal1 = parent1[0][:1]
        sinal2 = parent2[0][:1]

        #inteiro
        x1 = parent1[0][1:5]
        x2 = parent1[0][5:]

        y1 = parent2[0][1:5]
        y2 = parent2[0][5:]

        newx = x1 + y2
        newy = y1 + x2
        # print(newx,newy)


        #divisores
        a1 = parent1[1][:8]
        a2 = parent1[1][8:]

        b1 = parent2[1][:8]
        b2 = parent2[1][8:]

        newa = a1 + b2
        newb = b1 + a2

        # print(newa,newb)

        new_parent1 = sinal1+newx+'.'+newb
        new_parent2 = sinal2+newy+'.'+newa

        new_population.append(new_parent1)
        new_population.append(new_parent2)

        binary_parents.pop()
        binary_parents.pop()
    
    return new_population

binary_parents = ['000010000.0010011100000000', '001111000.1001100001110001', '100000001.0011100001110001', '000000001.0000000001010010', '000000001.1000000101010001', '000000010.0000000000000000'] 
new = crossover(binary_parents)
print(new)