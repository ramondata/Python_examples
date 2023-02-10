#! usr/bin/env python
# -*- coding: utf-8 -*-

from math import ceil
import sys, os

class amostra:

    def __init__(self):
        self.__n = 0.00
        self.__N = 0.00
        self.__p = 0.50
        self.__z = 1.96
        self.__e = 0.00
        
    @property 
    def N(self):
        self.__N = float(input("qual o tamanho da população?"))
        return self.__N
    
    @property
    def e(self):
        dado = float(input("qual o erro padrão?"))
        if(dado == 0.03):
            self.__e = dado
            return self.__e
        elif(dado == 0.05):
            self.__e = dado
            return self.__e
        else:
            return print("valor de erro inconsistente, precisa ser 3% ou 5%")
    
    def getN(self):
        return self.__N
    
    def getE(self):
        return self.__e
            
    def calcula_tamanho_amostra(self):
        c = (self.__z**2) * self.getN() * self.__p * (1.0-self.__p)
        d = ((self.__z**2) * self.__p * (1.0-self.__p)) + ((self.getN()-1.0) * (self.getE()**2))
        self.__n = c/d
        return print(f"Tamanho da amostra: {ceil(self.__n)}".center(100, "*"))
        
import calculador_de_amostra
from calculador_de_amostra import amostra

if(__name__ != "__main__"):
    pass
else:
	a = amostra()
	a.N
	a.e
	a.calcula_tamanho_amostra()