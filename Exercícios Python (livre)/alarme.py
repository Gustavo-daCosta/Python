from datetime import datetime
from playsound import playsound

texto = ''
try:
    texto = int(texto)
except:
    print('erro')
if isinstance(texto, int) is True:
    print('deu certo')