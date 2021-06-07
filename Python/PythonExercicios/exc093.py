dados = dict()
gols, total, gol = list(), 0, 0
dados['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for c in range(0, partidas):
    gol = (int(input(f'Quantos gols na partida {c+1}? ')))
    gols.append(gol)
    total += gol
dados.update({'gols': gols,
'total': total})
print('=-='*20)
print(dados)
print('=-='*20)
print(f'O campo nome tem o valor {dados["nome"]}')
print(f'O campo gols tem o valor {dados["gols"]}')
print(f'O campo total tem o valor {dados["total"]}')
print('=-='*20)
print(f'O jogador {dados["nome"]} jogou {partidas} partidas.')
for c in range(0, partidas):
    print(f'=> Na partida {c+1}, {dados["nome"]} fez {dados["gols"][c]} gols.')
print(f'Foi um total de {total} gols.')