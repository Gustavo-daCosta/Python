print('-='*20)
print('Analisador de Triângulos')
print('-='*20)
s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem formar um triângulo!')
    if s1==s2 and s2==s3 and s1==s3:
        print('Os segmentos formam um triângulo EQUILÁTERO')
    elif s1==s2 or s2==s3 or s1==s3:
        print('Os segmentos formam um triângulo ISÓSCELES')
    else:
        print('Os segmentos formam um triângulo ESCALENO')
else:
    print('Os segmentos acima não podem formar um triângulo!')