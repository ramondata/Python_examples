#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#   a. o produto do dobro do primeiro com metade do segundo .
#   b. a soma do triplo do primeiro com o terceiro.
#   c. o terceiro elevado ao cubo.

class numbers:

    def __init__(self):
        self.list_number = []

    i = 1

    def recebe_dados(self):
        global i
        for i in range(1, 2):
            while (i != 3):
                dado = int(input("Digite um numero INTEIRO"))
                self.list_number.insert(0, dado)
                i += 1
            else:
                dado = float(input("Digite um numero REAL"))
                self.list_number.insert(0, dado)
                i += 1
                
    def calculo_a(self):
        calc = (2*self.list_number[-1]) * (self.list_number[-2]/2)
        return calc
        
    def calculo_b(self):
        calc = (3*self.list_number[-1]) + self.list_number[-3]
        return calc
        
    def calculo_c(self):
        c = self.list_number[-3]
        calc = round(c*c*c, 2)
        return calc
        
#import num
#from num import numbers
        
if(__name__ == "__main__"):
    n = numbers()
    n.recebe_dados()
    n.calculo_a()
    n.calculo_b()
    n.calculo_c()