import sys
import math

class pintura:

    def __init__(self):
        self.__largura = 0.0
        self.__altura = 0.0
        self.__m2 = 0.0
        self.__litros = 0.0
        self.__latas = 0
        self.__custo = 0.0
    
    @property
    def largura(self):
        return self.__largura
        
    @property
    def altura(self):
        return self.__altura
        
    @property
    def m2(self):
        return self.__m2
    
    @property
    def litros(self):
        return self.__litros
        
    @property
    def latas(self):
        return self.__latas
    
    @property
    def custo(self):
        return self.__custo
    
    def setLargura(self):
            sys.stdout.write("Digite a largura: \n")
            into = sys.stdin
            dado = into.readline()
            self.__largura = float(dado)
    
    def setAltura(self):
            sys.stdout.write("Digite a altura: \n")
            into = sys.stdin
            dado = into.readline()
            self.__altura = float(dado)
            
    def calculaM2(self):
        self.__m2 = \
            self.__altura * self.__largura
    
    def calculaLitros(self):
        self.__litros = \
            self.__m2/3.0
            
    def calculaLatas(self):
        self.__latas = \
            self.__litros/18.0
            
    def calculaCusto(self):
        self.__custo = \
            self.__latas * 80.0
    
    def imprimeResultado(self):
        txt = """\nResultado final \nQuantidade de latas de tinta a comprar: {0} latas \nCusto total a ser pago pelas latas de tinta: {1} R$\n""".format(math.ceil(self.__latas), round(self.__custo,2))
        txt = txt.center(200,"*") 
        sys.stdout.write(f"{txt}")

    def imprimeGeral(self):
        sys.stdout.write("\n\n")
        sys.stdout.write(" Atributos: ".center(50, "*"))
        sys.stdout.write(f"\n{self.largura} largura")
        sys.stdout.write(f"\n{self.altura} altura")
        sys.stdout.write(f"\n{self.m2} metros quadrados")
        sys.stdout.write(f"\n{round(self.litros,1)} litros")
        sys.stdout.write(f"\n{math.ceil(self.latas)} latas")
        sys.stdout.write(f"\n{round(self.custo,2)} custo\n")
        sys.stdout.write("".center(50, "*"))
        
        
from pintar import pintura

if(__name__ != "__main__"):
    pass
else:
    a = pintura()
    a.setLargura()
    a.setAltura()
    a.calculaM2()
    a.calculaLitros()
    a.calculaLatas()
    a.calculaCusto()
    a.imprimeResultado()
    a.imprimeGeral()