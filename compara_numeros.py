#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Faça um Programa que peça dois números e imprima o maior deles.

import sys
import os
import math

class comparador_numerico:
    def __init__(self):
        self.__num1 = 0.0
        self.__num2 = 0.0
        self.__maior = 'numX'

    @property
    def num1(self):
        return self.__num1

    @property
    def num2(self):
        return self.__num2

    def entrada_numeros(self):
        sys.stdout.write("Digite o numero 1 ")
        dado1 = sys.stdin.readline()
        self.__num1 = float(dado1)
        sys.stdout.write("Digite o numero 2 ")
        dado2 = sys.stdin.readline()
        self.__num2 = float(dado2)
        return (self.__num1, self.__num2)

    def compara_numeros(self):
        if(self.__num1 > self.__num2):
            sys.stdout.write(" numero1: {0} é maior que numero2 {1} ".format(self.__num1, self.__num2))
        elif(self.__num1 < self.__num2):
            sys.stdout.write(" numero2: {1} é maior que numero1 {0} ".format(self.__num1, self.__num2))
        else:
            sys.stdout.write("os numeros são iguais ")

    def report(self):
        sys.stdout.write(" status report ".center(30, "*"))
        sys.stdout.write(" numero 1 digitado: {0} ".format(self.__num1))
        sys.stdout.write(" numero 2 digitado: {0} ".format(self.__num2))
        self.compara_numeros()
        sys.stdout.write("".center(30, "*"))

            
