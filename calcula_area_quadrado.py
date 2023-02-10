#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

class quadrado(object):

    def __init__(self):
        self.lado = 0.0
        self.area = 0.0
        
    def pede_lado(self):
        self.lado = round(float(input("Qual a medida lateral do quadrado ? \n")),2)
        return self.lado
        
    def calcula_area(self):
        self.area = round(self.lado*self.lado*2, 2)
        return print(f"O dobro da area do quadrado de lado {self.lado} é {self.area}")
        
from quadrado import*

if(__name__=="__main__"):
    quad1 = quadrado()
    quad1.pede_lado()
    quad1.calcula_area()