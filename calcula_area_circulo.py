#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

class circulo(object):

    def __init__(self):
        self.raio = 0
        self.area = 0
        return print("método construtor utilizado, objeto instanciado")

    def solicita_raio(self):
        valor = float(input("Insira o valor do raio do circulo \n"))
        self.raio = valor
        return print(f"Raio no valor de {self.raio}")

    def calcula_area(self):
        self.area = round(3.1415 * self.raio * self.raio,2)
        return print(f"Area do circulo de raio {self.raio} igual a {self.area}")