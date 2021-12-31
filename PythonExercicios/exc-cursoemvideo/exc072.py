num_extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', "Oito", 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    n = int(input('Digite um número: '))
    if n >= 0 and n <= 20:
        print(f'O número {n} por extenso é: {num_extenso[n]}')
        break
    else:
        print('Número inválido! Tente novamente.')