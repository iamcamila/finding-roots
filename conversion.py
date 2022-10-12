
x = '1001'
r = int(x,2)
# print(r)

def tobinario(y):
    ybint = '0'
    ybdec = '0'

    if y>=0:
        sinal = '0'
    else:
        sinal = '1'

    y = str(y)
    y = y.split('.')
    if len(y) > 1:
        ybint = bin(int(y[0])).replace('0b','')
        ybdec = bin(int(y[1])).replace('0b','')
    else:
        ybint = bin(int(y[0])).replace('0b','')

    while len(ybdec) % 4 !=0:
        ybdec = '0'+ ybdec

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
        yddec = int(y[1],2)

    decimal = str(ydint)+'.'+str(yddec)
    decimal = float(decimal)*sinal
    return decimal
