num = [2, 5, 9, 1, 8]
num[2] = 3
# Diferente das Tuplas, as Listas são MUTÁVEIS.

num.append(7)
# .APPEND() = Adiciona um novo valor a Lista em questão.

num.sort()
# .SORT() = Se todos os valores da lista forem numéricos, ele coloca os valores da lista do menor valor para o maior.

num.sort(reverse=True)
# .SORT(REVERSE = TRUE) = Coloca os valores da lista do MAIOR valor para o MENOR.

num.insert(2, 0)
# .INSERT() = Insere um valor em uma posição específica. No exemplo acima, o comando está inserindo na posição 2, o valor 0.

num.pop()
# .POP = Elimina o último elemento da lista. Se houver valor nos parênteses o comando vai mudar o valor da posição dos parênteses para 0.

num.remove(2)
# .REMOVE() = Remove a primeira ocorrência do número colocado entre parênteses

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')

print(num)
print(f'Essa lista tem {len(num)} elementos')