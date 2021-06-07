from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(ang))
print(f'O ângulo de {ang} tem o seno de {seno:.2f}')
cosseno = cos(radians(ang))
print(f'O ângulo de {ang} tem o cosseno de {cosseno:.2f}')
tangente = tan(radians(ang))
print(f'O ângulo {ang} tem a tangente de {tangente:.2f}')