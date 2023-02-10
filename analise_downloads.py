#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import math
import sys
import os
import datetime

class download:

    def __init__(self):
        self.__tamanho_arq = 0.0
        self.__velocidade = 0.0
        self.__tempo = 0.0
        self.__dict_unidades = {'arquivo' : 'MB', 'velocidade' : 'Mbps', 'tempo' : 'Min'}

    @property
    def tamanho_arq(self):
        return sys.stdout.write("{0} {1}".format(self.__tamanho_arq, self.__dict_unidades['arquivo']))

    @property
    def velocidade(self):
        return sys.stdout.write("{0} {1}".format(self.__velocidade, self.__dict_unidades['velocidade']))

    @property
    def tempo(self):
        return sys.stdout.write("{0} {1}".format(self.__tempo, self.__dict_unidades['tempo']))

    def setTamanho(self):
        sys.stdout.write("Tamanho do arquivo: ")
        into = sys.stdin
        dado = into.readline()
        self.__tamanho_arq = float(dado)

    def setVelocidade(self):
        sys.stdout.write("Velocidade do download: ")
        into = sys.stdin
        dado = into.readline()
        self.__velocidade = float(dado)

    def calcula_tempo(self):
        self.__tempo = round(self.__tamanho_arq / (self.__velocidade * 7.5), 2)

    def apresenta_resultados(self):
        sys.stdout.write("________ Apresentação de resultados _______")
        sys.stdout.write("\n")
        sys.stdout.write("Tamanho do arquivo: {0} {1}".format(self.tamanho_arq, self.__dict_unidades['arquivo'])) 
        sys.stdout.write("\n")
        sys.stdout.write("Velocidade de download: {0} {1}".format(self.velocidade, self.__dict_unidades['velocidade']))
        sys.stdout.write("\n")
        sys.stdout.write("Tempo do download: {0} {1}".format(self.tempo, self.__dict_unidades['tempo']))
        sys.stdout.write("\n")
        sys.stdout.write("-------------------------------------------")
