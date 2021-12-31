titulo, msg, tipo = 'ANÁLISE DE TRIÂNGULOS', 'Não é possível formar um triângulo.', ''
print('-'*40)
print(f'{titulo:^40}')
print('-'*40)
reta1 = int(input('Comprimento da 1° reta: '))
reta2 = int(input('Comprimento da 2° reta: '))
reta3 = int(input('Comprimento da 3° reta: '))
if (reta1 + reta2) > reta3:
    if (reta1 + reta3) > reta2:
        if (reta3 + reta2) > reta1:
            msg = 'É possível formar um triângulo!'
if reta1 == reta2 and reta2 == reta3 and reta1 == reta3:
    tipo = 'Equilátero'
if reta1 != reta2 and reta2 != reta3 and reta1 != reta3:
    tipo = 'Escaleno'
if tipo != 'Equilátero':
    if reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        tipo = 'Isósceles'
print(msg)
if msg not in ('Não é possível formar um triângulo.'):
    print(f'Tipo de triângulo: Triângulo {tipo}')