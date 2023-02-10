#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

class altura_ideal:

    def __init__(self):
        self.sexo = 'a'
        self.altura = 0.0
        self.peso = 0.0
        self.imc = 0.0
        self.alt_ideal = 0.0
        imc_ideal = 22.0
        print("método construtor utilizado")



    def recebe_dados(self):
        self.peso = float(input("Insira seu peso \n"))
        self.altura = float(input("Insira sua altura \n"))
        self.sexo = input("Insira o sexo m ou f \n")
        return (self.altura, self.peso, self.sexo)

    def calcula_imc(self):
        self.imc = self.peso / self.altura * self.altura
        return self.imc

    def calcula_altura(self, imc_ideal=22.0):
        import math
        if (self.sexo == 'm'):
            if (self.imc <= 18.50 or self.imc >= 24.99):
                self.alt_ideal = round(math.sqrt(self.peso / imc_ideal),2)
            else:
                self.altura = math.sqrt(self.peso / self.imc)
        elif (self.imc <= 16.50 or self.imc >= 21.99)
            self.alt_ideal = round(math.sqrt(self.peso / imc_ideal),2)
import alt
from alt import altura_ideal

if(__name__ != "__main__"):
    pass
else:
    i = altura_ideal()
    i.recebe_dados()
    i.calcula_imc()
    i.calcula_altura()
    print(f"altura: {i.altura}")
    print(f"altura_ideal: {i.alt_ideal}")