def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA'
    if idade == 16 or idade == 17 or idade >= 60:
        return f'Com {idade} anos: VOTO OPCIONAL'
    if idade >= 18 and idade < 60:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'

print('-'*30)
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))
print('-'*30)