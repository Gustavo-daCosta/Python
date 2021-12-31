from urllib import request

try:
    request.urlopen('http://pudim.com.br')
except request.URLError:
    print('O site Pudim não está acessivel no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')