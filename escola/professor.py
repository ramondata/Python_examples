#!/usr/bin/env python

import escola
import sys
import os
import math

class professor(escola.escola):
    def __init__(self, nome, idade, materia_leciona):
        super().__init__(nome, idade)
        self.__materia_leciona = materia_leciona

    @property
    def materia_leciona(self):
        return self.__materia_leciona

    @materia_leciona.setter
    def materia_leciona(self, materia):
        self.__materia_leciona = materia

    @staticmethod
    def nome_da_classe():
        info = 'professor'
        return info
