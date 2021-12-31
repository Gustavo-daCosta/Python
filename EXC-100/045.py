inicio = int(input('Digite o primeiro valor: '))
final = int(input('Digite o último valor: '))
inc = int(input('Digite o incremento: '))
if inc == 0:
    inc = 1
if final < inicio and inc > 0:
    inc = inc*-1
print('-'*40)
print('Contagem:', end=' ')
for c in range(inicio, final+1, inc):
    print(c, end=' ')
print('Acabou!')