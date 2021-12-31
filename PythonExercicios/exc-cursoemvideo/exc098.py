from time import sleep

def contagem(a, b, c):
    print('=-='*20)
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    for cont in range(a, b, c):
        print(cont, end=' → ', flush=True)
        sleep(0.3)
    print('FIM!')

contagem(1, 10, 1)
contagem(10, 0, -2)
print('=-='*20)
print('Agora é sua vez de personalizar a contagem!')
contagem(
    a = int(input('Início: ')),
    b = int(input('Fim: ')),
    c = int(input('Passo: '))
)