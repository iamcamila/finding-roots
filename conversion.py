
def tobinario(y):
    ybint = ''
    ybdec = ''

    if y>=0:
        sinal = '0'
    else:
        sinal = '1'

    y = str(y)
    y = y.split('.')
    if len(y) > 1:
        inteiro = y[0]
        # print(inteiro)
        if sinal == '1':
            inteiro = y[0][1:]
            # print(inteiro)
        ybint = bin(int(inteiro)).replace('0b','')
        
        for num in y[1]:
            num = bin(int(num)).replace('0b','')
            while len(num) % 4 !=0:
                num = '0'+ num
            ybdec += num

    else:
        ybint = bin(int(y[0])).replace('0b','')

    while len(ybdec) % 4 !=0:
        ybdec = '0'+ ybdec
    
    while len(ybint) % 4 !=0:
        ybint = '0'+ ybint

    #padronizar tamanho binário

    while len(ybint)<8:
        ybint = '0'+ ybint
        
    while len(ybdec)<16:
        ybdec = ybdec + '0'

    binario = sinal + ybint + '.' + ybdec
    return binario

def todecimal(y):
    if y[0] == '1':
        sinal = -1
    else:
        sinal = 1

    y = y[1:]
    y = y.split('.')
    if len(y) > 1:
        ydint = int(y[0],2)
        a1 = int(y[1][:4], 2)
        a2 = int(y[1][4:8],2)
        a3 = int(y[1][8:12],2)
        a4 = int(y[1][12:16],2)
        yddec = str(a1)+str(a2)+str(a3)+str(a4)

    decimal = str(ydint)+'.'+str(yddec)
    # decimal = int(decimal,2)
    decimal = float(decimal)*sinal
    return decimal
