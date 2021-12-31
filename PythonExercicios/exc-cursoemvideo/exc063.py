n = int(input('Você deseja ver quantos elementos da sequência de Fibbonaci? '))
ultimo = 1
penultimo = 1
if (n==1) or (n==2):
    print('1')
else:
    count = 3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
        print(f'{ultimo} → ', end='')
    print('FIM')