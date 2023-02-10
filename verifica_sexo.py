#!/usr/bin/env python
# -*- encoding: utf-8 -*-


#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

import sys
import os
import math

class sexo:
    def __init__(self):
        self.__sexo = 'fm'
        self.__ident = 'feminino'

    @property
    def sexo(self):
        return self.__sexo

    def entrada_dados(self):
        sys.stdout.write("Digite M para masculino e F para feminino ")
        dado = sys.stdin.readline()
        dado = dado[0].lower()
        self.__sexo = dado

    def verificador(self):
        if(self.__sexo == 'm'):
            self.__ident = 'masculino'
        elif(self.__sexo == 'f'):
            self.__ident = 'feminino'
        else:
            self.__ident = 'não identificado'

    def resultado(self):
        string_final = 'O valor informado foi {0}.\n{0} Corresponde ao sexo {1} '.format(self.__sexo, self.__ident)
        return sys.stdout.write(string_final)

