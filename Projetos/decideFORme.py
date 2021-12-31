from random import randint

positivo, talvez, negativo = list(), list(), list()
positivo = ['Sim, vai lá!', 'Acredito que sim', 'É claro!', 'Obviamente que sim', 'Sim.', 'Óbvio que sim', 
'Você precisa fazer isso', 'Creio que sim', 'SIM! SIM! SIM!', 'Sem sombra de dúvidas', 'Por que não?', 'Eu aprovo']
negativo = ['Não vá.', 'Não acho necessário', 'Creio que não', 'Não.', 'Considere isso um não', 'Definitivamente não',
'Pode apostar que não', 'Negativo.', 'Não me parece certo', 'Por favor, não.', 'Nunca', 'Não faça isso']
talvez = ['Não tenho certeza', 'Não posso decidir isso', 'Talvez', 'Pode ser que sim, pode ser que não', 'Não sei', 'Não tenho uma resposta']

while True:
    lista = randint(1, 3)
    if lista == 1:
        resp = positivo[randint(0, 11)]
    elif lista == 3:
        resp = negativo[randint(0, 11)]
    else:
        resp = talvez[randint(0, 5)]
    print(f'DECIDA POR MIM'.center(40, '='))
    perg = str(input('Faça sua pergunta: '))
    print(f'Resposta: {resp}')
    print('='*40)
    print()
    while True:
        opcao = str(input('Deseja continuar? [S/N]: ')).upper()
        if opcao in 'SN':
            break
        else:
            print('ERRO! Digite uma opção válida')
    if opcao == 'N':
        break
print('Volte sempre!')