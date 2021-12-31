# DESAFIO !
'''
Você irá criar a class Carro e adicionar a classe ao menos 3 propriedades e 3 métodos
'''

class Carro:
    def __init__(self, velMax, velAtual, modelo, ano, cor):
        self.velMax = velMax
        self.velAtual = velAtual
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.ligado = False

    def Ligar(self):
        self.ligado = True
    
    def Desligar(self):
        self.ligado = False
    
    def velocidadeAtual(self, velAtual):
        self.velAtual = velAtual