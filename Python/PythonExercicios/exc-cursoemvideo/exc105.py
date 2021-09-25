def notas(* nota, sit=False):
    """[Função para analisar notas e situações de vários alunos.]

    Args:
        nota (float, multiple): [uma ou mais notas dos alunos.]
        sit (bool, optional): [Indica se deve ou não mostrar a situação]. Defaults to False.

    Returns:
        [dict]: [dicionário com várias informações sobre a turma.]
    """
    dicio = dict()
    total = len(nota)
    soma = sum(nota)
    maior = max(nota)
    menor = min(nota)
    media = soma/total
    if media < 5:
        situacao = 'Péssima'
    if media >= 5 and media < 7:
        situacao = 'Ruim'
    if media >= 7 and media < 8:
        situacao = 'Boa'
    if media >= 8:
        situacao = 'Ótima'
    dicio = {
        'Quantidade de notas': total,
        'Maior nota': maior,
        'Menor nota': menor,
        'Média da Turma': media,
        'Situação': situacao
    }
    return dicio

resp = notas(5, 9.5, 7.3, 4.6, 2, 9.5, sit=True)
print(resp)
help(notas)