def ficha(nome='<desconhecido>', gols=0):
    if nome.strip() == '':
        nome = '<desconhecido>'
    if gols.strip() == '':
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'

nome = str(input('Nome do jogador: '))
gols = str(input('Número do gols: '))
print(ficha(nome, gols))