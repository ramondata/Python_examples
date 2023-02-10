#!usr/bin/env python3
# -*- encoding: utf-8 -*-

#Crie um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

import sys
import os
import math

class sinal:
    def __init__(self):
        self.__numero = 0.0
        self.__sinal = '+'

    @property
    def numero(self):
        return self.__numero

    @property
    def sinal(self):
        return self.__sinal

    def pede_numero(self):
        sys.stdout.write("Digite seu numero com o sinal, por favor: \n")
        numero = float(sys.stdin.readline())
        self.__numero = numero
        return sys.stdout.write("Numero com sinal escolhido foi {0} \n".format(numero))

    def verifica_sinal(self):
        sinal = str(self.__numero)
        if(sinal[0] == '-'):
            self.__sinal = sinal[0]
        else:
            self.__sinal

    def resultado(self):
        return sys.stdout.write("O sinal do numero digitado é {0} \nNumero digitado é {1}".format(self.__sinal, self.__numero))

