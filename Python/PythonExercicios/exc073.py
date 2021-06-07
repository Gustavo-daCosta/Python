times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG', 'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG', 'Vitória', 'Paraná')
cont, opcao, continuar = 0, 0, 'S'
while continuar == 'S':
    print('=-='*20)
    print('         BRASILEIRÃO 2021')
    print('=-='*20)
    print('[ 1 ] MOSTRAR OS 5 PRIMEIROS COLOCADOS')
    print('[ 2 ] MOSTRAR OS 4 ÚLTIMOS COLOCADOS')
    print('[ 3 ] MOSTRAR OS TIMES EM ORDEM ALFABÉTICA')
    print('[ 4 ] MOSTRAR A COLOCAÇÃO DO CHAPECOENSE')
    opcao = int(input('Digite sua opção: '))
    if opcao == 1:
        cont = 0
        while cont != 5:
            print(f'O {cont+1}° colocado da tabela é o {times[cont]}')
            cont += 1
    if opcao == 2:
        cont = 16
        while cont != 20:
            print(f'O {cont+1}° colocado da tabela é o {times[cont]}')
            cont = cont + 1
    if opcao == 3:
        cont = 0
        ordem_alfa = sorted(times)
        print('TIMES EM ORDEM ALFABÉTICA:')
        while cont != 20:
            print(ordem_alfa[cont], end=' → ')
            cont += 1
        print('FIM')
    if opcao == 4:
        chapecoense = times.index('Chapecoense')
        print(f'O Chapecoense está na {chapecoense}° posição da tabela.')
    continuar = str(input('Você deseja continuar? [S/N] ')).upper()
print('Programa finalizado! Volte sempre.')