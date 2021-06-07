n1 = int(input('Digite a sua primeira nota: '))
n2 = int(input('Digite a sua segunda nota: '))
media = (n1+n2)/2
if media<=5.0:
    print(f'Média do aluno: {media}   Status do aluno: REPROVADO.')
elif media>5.0 and media<7.0:
    print(f'Média do aluno: {media}   Status do aluno: RECUPERAÇÃO.')
else:
    print(f'Média do aluno: {media}   Status do aluno: APROVADO.')