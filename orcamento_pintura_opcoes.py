#Faça um Programa para uma loja de tintas. 
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
#que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. 
#Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import sys
import os
import math

class comprar_tinta:

    def __init__(self):
        self.__altura = 0.0
        self.__largura = 0.0
        self.__area = 0.0
        self.__litros = 0.0
        self.__latas_18 = 0
        self.__latas_3f6 = 0
        self.__latas_perform = 0
        self.__custo_18 = 0.0
        self.__custo_3f6 = 0.0
        self.__custo_perform = 0.0
        self.__part1 = 0.0
        self.__part2 = 0.0
 
    @property
    def altura(self):
        sys.stdout.write("Qual a altura da parede para pintura? ")
        entrada = sys.stdin
        dado = entrada.readline()
        self.__altura = float(dado)
    
    @property
    def largura(self):
        sys.stdout.write("Qual a altura da parede para pintura ? ")
        entrada = sys.stdin
        dado = entrada.readline()
        self.__largura = float(dado)
    
    @property
    def area(self):
        self.__area = self.__largura * self.__altura
    
    @property
    def litros(self):
        self.__litros = self.__area / 6.0
    
    @property
    def latas_18(self):
        self.__latas_18 = math.ceil(self.__litros / 18)
    
    @property
    def latas_3f6(self):
        self._latas_3f6 = math.ceil(self.__litros / 3.6)
   
    @property
    def latas_perform(self):
        if(self.__litros % 18 == 0):
            self.__latas_perform = math.ceil(self.__litros / 18)
        elif(self.__litros % 18 != 0):
            self.__part_1 = self.__litros - (self.__litros % 18)
            self.__part_2 = math.ceil(self.__litros % 18)
            self.__latas_perform = self.__part1 + self.__part2
        else:
            print("Reveja o código da func latas_perform")
    
    @property
    def custo_18(self):
        self.__custo_18 = self.__latas_18 * 80.0
    
    @property
    def custo_3f6(self):
        self.__custo_3f6 = self.__latas_3f6 * 25.0
    
    @property
    def custo_perform(self):
        self.__custo_perform = (self.__part1 * 80.0) + (self.__part2 * 25.0)
   
    def getAltura(self):
        return self.__altura
   
    def getLargura(self):
        return self.__largura
    
    def getArea(self):
        return self.__area
    
    def getLitros(self):
        return self.__litros

    def getLatas_18(self):
        return self.__latas_18

    def getLatas_3f6(self):
        return self.__latas_3f6
   
    def getLatas_perform(self):
        return self.__latas_perform
    
    def getCusto_18(self):
        return self.__custo_18
    
    def getCusto_3f6(self):
        return self.__custo_3f6

    def getCusto_perform(self):
        return self.__custo_perform
   

if(__name__ != "__main__"):
    pass
else:
    obj = comprar_tinta()
    obj.altura
    obj.largura
    obj.area
    obj.litros
    obj.latas_18
    obj.latas_3f6
    obj.latas_perform
    obj.custo_18
    obj.custo_3f6
    obj.custo_perform

