#!/usr/bin/env python

import escola
import sys
import os
import math

class aluno(escola.escola):
    def __init__(self, nome, idade, materia_preferida):
        super().__init__(nome, idade)
        self.__materia_preferida = materia_preferida

    @property
    def materia_preferida(self):
        return self.__materia_preferida

    @materia_preferida.setter
    def materia_preferida(self, materia_preferida):
        self.__materia_preferida = materia_preferida

    @staticmethod
    def nome_da_classe():
        info = 'aluno'
        return info
