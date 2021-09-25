from datetime import date   
data = date.today().year
maior18 = 0
menor18 = 0
for c in range(1,8):
    nasc = int(input(f'Digite o ano de nascimento da {c}° pessoa: '))
    idade = data - nasc
    if idade >= 21:
        maior18 += 1
    else:
        menor18 += 1
print(f'Quantidade de pessoas MAIORES de 21 anos: {maior21}')
print(f'Quantidade de pessoas MENORES de 21 anos: {menor21}')