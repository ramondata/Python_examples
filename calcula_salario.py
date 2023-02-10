#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

class salario:

    def __init__(self):
        self.ganho_hora = 0.0
        self.total_horas = 0.0
        self.salario = 0.0

    def valor_hora(self):
        valor = float(input("Quanto ganha por hora?"))
        self.ganho_hora = valor
        return self.ganho_hora

    def horas(self):
        valor = float(input("Quantas horas trabalhou no mes?"))
        self.total_horas = valor
        return self.total_horas

    def calcula_salario(self):
        self.salario = self.ganho_hora * self.total_horas
        return print(f" salario: {self.salario}".center(50, "*"))

from salario import *

if (__name__ == "__main__"):
    func1 = salario()
    func1.valor_hora()
    func1.horas()
    func1.calcula_salario()