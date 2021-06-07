from time import sleep
cont, n = 0, 0
while n >= 0:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)
    if n <= -1:
        break
    while cont != 10:
        cont += 1
        print(f'{n} x {cont} = {n*cont}')
        sleep(0.1)
    cont = 0
    print('-'*30)
print('PROGRAMA DE TABUADA ENCERRADO.')