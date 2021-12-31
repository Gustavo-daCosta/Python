anterior = sucessor = 0
for c in range(0, 10):
    print(sucessor, end=' ')
    sucessor = sucessor + anterior
    anterior = sucessor - anterior
    if sucessor == 0:
        sucessor += 1
print('FIM!')