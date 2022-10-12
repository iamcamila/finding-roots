
binary_parents = ['10.00010100100010101010111000001010100100101110100101111111', '01.00010001000111000010010110000101110101011100001010101101', '00.01010101111101001111001000000011011011000000000011110110', '00.01001001101101111101101001110000100000110000010001000110']
new_population = []

while len(binary_parents) != 0:

    parent1  = binary_parents[0].split('.')
    parent2 = binary_parents[1].split('.')

    #inteiro
    x1 = parent1[0][:1]
    x2 = parent1[0][1:]

    y1 = parent2[0][:1]
    y2 = parent2[0][1:]

    newx = x1 + y2
    newy = y1 + x2
    # print(newx,newy)


    #divisores
    a1 = parent1[1][:28]
    a2 = parent1[1][28:]

    b1 = parent2[1][:28]
    b2 = parent2[1][28:]

    newa = a1 + b2
    newb = b1 + a2

    # print(newa,newb)

    new_parent1 = newx+newb
    new_parent2 = newy+newa

    new_population.append(new_parent1)
    new_population.append(new_parent2)

    binary_parents.pop()
    binary_parents.pop()
    print(new_population)