menor = 0
maior = 0
for c in range(1,6):
    peso = int(input(f'Digite o peso da {c}° pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    if peso < menor:
        menor = peso
    if peso > maior:
        maior = peso
print(f'O MAIOR peso registrado foi: {maior:.1f} kg')
print(f'O MENOR peso registrado foi: {menor:.1f} kg')