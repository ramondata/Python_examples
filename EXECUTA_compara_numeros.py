#!/usr/bin/env python

import compara_numeros
from compara_numeros import comparador_numerico

if(__name__ != "__main__"):
    pass
else:
    obj = comparador_numerico()
    obj.entrada_numeros()
    obj.compara_numeros()
    obj.report()

    print("___")
    obj.num1
    obj.num2
