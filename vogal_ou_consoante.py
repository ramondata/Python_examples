#!/usr/bin/env python
# -*- encoding: utf-8 -*-

#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

import sys
import os
import math

class letra:

    def __init__(self):
        self.__letra = 'A'
        self.__tipo = 'vogal'
        self.__list_vogal = 'A,E,I,O,U'.split(",")
        self.__list_consoante = 'B,C,D,F,G,H,J,K,L,M,N,P,Q,R,S,T,V,Y,W,Ç,X,Z'.split(",")

    @property
    def letra(self):
        return self.__letra

    @property
    def tipo(self):
        return self.__tipo

    def entrada_dados(self):
        sys.stdout.write("Digite a letra que deseja verificar se é vogal ou consoante :")
        dado = sys.stdin.readline()
        self.__letra = dado[0].upper()

    def verificador(self):
        if( self.__letra in self.__list_vogal):
            self.__tipo = 'Vogal'
        elif( self.__letra in self.__list_consoante):
            self.__tipo = 'Consoante'

    def resultado(self):
        string_letra = 'A letra informada foi {0}'.format(self.__letra)
        string_tipo = ' o tipo de letra digitada é {0}'.format(self.__tipo)
        print(string_letra)
        print(string_tipo)

