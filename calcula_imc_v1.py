#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#usando a seguinte fórmula: (72.7*altura) - 58

class altura_ideal:

    def __init__(self):
        self.altura = 0.0
        self.peso = 0.0
        self.imc = 0.0
        self.alt_ideal = 0.0
        imc_ideal = 22.0
        print("método construtor utilizado")



    def recebe_dados(self):
        self.peso = float(input("Insira seu peso \n"))
        self.altura = float(input("Insira sua altura \n"))
        return (self.altura, self.peso)

    def calcula_imc(self):
        self.imc = self.peso / self.altura * self.altura
        return self.imc

    def calcula_altura(self, imc_ideal=22.0):
        import math
        if (self.imc <= 18.50 or self.imc >= 24.99):
            self.alt_ideal = round(math.sqrt(self.peso / imc_ideal),2)
        else:
            self.altura = math.sqrt(self.peso / self.imc)
        
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