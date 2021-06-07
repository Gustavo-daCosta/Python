from math import sqrt
opos = int(input('Digite o tamanho do cateto oposto: '))
adja = int(input('Digite o tamanho do cateto adjacente: '))
hip = sqrt(opos*opos + adja*adja)
print (f'A hipotenusa é {hip:.2f}')