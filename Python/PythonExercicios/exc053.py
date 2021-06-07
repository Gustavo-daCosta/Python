palin = str(input('Digite a frase que você deseja verificar se é um palíndromo: ')).upper().replace(" ", "")
if palin == palin[::-1]:
    print('Essa frase É UM PALÍNDROMO')
else:
    print('Essa frase NÃO É UM PALÍNDROMO')