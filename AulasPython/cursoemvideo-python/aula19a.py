pessoas = { 'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
# DICIONÁRIOS são declarados com chaves {}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')

print(pessoas.keys())
for k in pessoas.keys():
    print(k)
# dict.KEYS = Mostra somente as chaves do dicionário

print(pessoas.values())
for k in pessoas.values():
    print(k)
# dict.VALUES = Mostra somente os valores do dicionário

print(pessoas.items())
for k in pessoas.items():
    print(k)
# dict.ITEMS = Mostra tudo que está no dicionário, incluindo chaves e valores

del pessoas['nome']
# DEL = Deleta a chave que está entre colchetes, e o valor contido na chave

pessoas['nome'] = 'Leandro'
# Subtitui o valor da chave entre colchetes, no caso"nome"

for k, v in pessoas.items():
    print(f'{k} = {v}')