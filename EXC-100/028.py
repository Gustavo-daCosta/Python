titulo = 'ANÁLISE DE TERRENOS'
print('-'*50)
print(f'{titulo:^50}')
print('-'*50)
print('Terreno com menos de 100m² = TERRENO POPULAR')
print('Terreno entre 100m² e 500m² = TERRENO MASTER')
print('Terreno acima de 500m² = TERRENO VIP')
print('-'*50)
largura = float(input('Digite a largura do terreno: '))
altura = float(input('Digite a altura do terreno: '))
area = largura * altura
if area < 100:
    classif = 'TERRENO POPULAR'
if area >= 100 and area <= 500:
    classif = 'TERRENO MASTER'
if area > 500:
    classif = 'TERRENO VIP'
print('-'*50)
print(f'Área do terreno: {area}m²')
print(f'Classificação do terreno: {classif}')