a = [2, 3, 4, 7]
b = a

print(f'Lista A: {a}')
print(f'Lista B: {b}')

# ATENÇÃO! Quando se cria uma váriavel e da o valor de uma lista a ela, você cria uma ligação entre as duas, como no exemplo "b = a" (a é uma lista).
# Se você alterar qualquer valor na lista a, a lista b será automaticamente alterada.

# Para criar um clone de uma lista que não tenha ligação nenhuma com a original você deve seguir os passos abaixo:
a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
 # CÓPIA DE LISTAS = Você deve usar o "(cópia) = (original)[:]" assim como no exemplo acima.

print(f'Lista A: {a}')
print(f'Lista B: {b}')