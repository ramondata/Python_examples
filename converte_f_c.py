#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

class temperatura:

    def __init__(self):
        self.c = 0.0
        self.f = 0.0
        print("objeto instânciado")

    def recebe_f(self, valor):
        self.f = valor
        return print(self.f)

    def converte_f_para_c(self):
        if (self.f <= -100.0):
            print("pare de savanagem")
        elif (self.f >= 500.0):
            print("pare de sacanagem")
        else:
            self.c = 5 * ((self.f - 32.0) / 9)
        return print(f"temperatura em °C: {self.c} \n")
        
import temp
from temp import temperatura

if __name__ != "__main__":
        pass
else:
        temp1 = temperatura()
        temp2 = temperatura()

        temp1.recebe_f(35.7)
        temp2.recebe_f(49.0)

        temp1.converte_f_para_c()
        temp2.converte_f_para_c()