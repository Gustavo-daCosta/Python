frase = str(input('Digite uma frase: ')).lower()
print(f'A letra "a" aparece {(frase.count("a"))} vezes na frase')
print(f'A primeira letra "a" apareceu na posição {frase.find("a")+1}')
print(f'A última letra "a" apareceu na posição {frase.rfind("a")+1}')