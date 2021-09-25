print('='*20)
print('')
casa = int(input('Qual é o valor do imóvel R$'))
verb = int(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você pretende pagar a casa? '))
teto = (verb*0.30)
parc = (casa/(anos*12))
if parc>teto:
    print('Seu empréstimo não foi aprovado.')
else:
    print('Seu empréstimo foi aprovado.')