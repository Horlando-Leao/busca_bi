from random import randint

n_min = 1
n_max = 1000

in_ = (n_min, n_max)
ns = int(randint (n_min, n_max))
mi_s = in_[0]
ma_s = in_[1]

x = int(in_[1] /2)
print('chute =', x)

def verificar(y, ns):
    if y == ns:
        print('o programa tira onda')
    elif y != ns:
        bingo(x, y, ns, ma_s)

def bingo(x, y, ns, ma_s):

    if ns > x:
        print('ns > x')
        y = int((ma_s - x)/2) 
        print('chute =',y)

        if y > x:
            print('y > x')
            y = int((y - x)/ 2)
            print('chute =',y)
            verificar(y, ns)

        elif y < x:
            print(' y < x')
            y = int(( x - y)/2)
            print('chute =',y)
            verificar(y, ns)

        elif y == ns:
            print('numero sorteado = ',y)
                

    elif ns < x:
        print('ns < x')
        y = int((x/2))
        print('chute =',y)

        if y > x:
            print('y > x')
            y = int((x -y)/2)
            print('chute =',y)
            verificar(y, ns)

        elif y < x:
            print('y < x')
            y = int((y/2))
            print('chute =',y)
            verificar(y, ns)

        elif y == ns:
            print('numero sorteado = ',y)
                
    return y

    verificar(y, ns)

bingo(x, y=x, ns=ns, ma_s=ma_s)
        
