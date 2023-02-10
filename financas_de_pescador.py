#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite 
#e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

class financas_pesca:

    def __init__(self):
        self.peso = 0.0
        self.multa = 0.0
        self.excesso = 0.0

    def recebe_peso(self):
        peso = float(input("Insira o peso dos peixes: "))
        self.peso = peso

    def analisa_excesso(self):
        if (self.peso < 50.0):
            self.excesso = 0.0
        elif (self.peso == 50.0):
            self.excesso = 0.0
        elif (self.peso > 50.0):
            self.excesso = self.peso - 50.0
        return self.excesso

    def valor_multa(self):
        self.multa = self.analisa_excesso() * 4.0

    def resultado(self):
        return print(
            f"Peso dos peixes: {self.peso} \nExcesso de quilos: {self.excesso} \nMulta a ser paga: {self.multa}")

if(__name__ != "__main__"):
    pass
else:
    a = financas_pesca()
    a.recebe_peso()
    a.analisa_excesso()
    a.multa()
    a.resultado()