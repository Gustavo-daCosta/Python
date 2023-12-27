from os import system
from random import randint
from time import sleep

# chr()

fraseSendoEscrita = True

caracteres = [chr(valor) for valor in range(32, 127)]
simbolos = [chr(valor) for valor in range(161, 192)]

valores = caracteres + simbolos

#valoresAscii = [valor for valor in valores if r"\x" not in valor]
#valoresAscii = [valor for valor in valores if r"\x" not in r"{}".format(f"{valor}")]
#print(valores)

frase = "hello world".split()

for letra in frase:
  
  
# hello world com valores sendo substituidos pelas letras com o tempo