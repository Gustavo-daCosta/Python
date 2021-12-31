consoantes, caract = [], 0
for c in range(0, 10):
    caract = str(input(f'Digite o {c+1}° caractere: ').lower())
    if caract not in 'aeiou':
        consoantes.append(caract)
print('=-='*15)
print(f'Total de consoantes digitadas: {len(consoantes)}')
print(f'As consoantes digitadas foram: {consoantes}')