print('='*25)
print('     ALISTAMENTO MILITAR')
print('='*25)
idade = int(input('Digite sua idade atual: '))
if idade<18:
    print('Você ainda não tem idade suficiente para se alistar.')
    print(f'Faltam {18-idade} anos para você estar apto para se alistar.')
elif idade>18:
    print('Você já passou da idade para se alistar.')
    print(f'Se passaram {idade-18} anos do prazo de alistamento.')
elif idade==18:
    print('Você tem a idade certa para se alistar!')