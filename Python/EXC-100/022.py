print('=-=-=-=-= ALISTAMENTO MILITAR =-=-=-=-=')
nasc = int(input('Digite seu ano de nascimento: '))
idade = 2021 - nasc
if idade < 18:
    print('Você não tem idade o suficiente para se alistar!')
    print(f'Faltam {18-idade} anos para você se alistar.')
elif idade > 18:
    print('Você passou da idade suficiente para se alistar!')
    print(f'Passaram {idade-18} anos da idade de alistamento.')
else:
    print('Você tem a idade certa para se alistar!')