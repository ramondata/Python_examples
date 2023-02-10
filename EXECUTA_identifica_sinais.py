#!/usr/bin/env python

from identifica_sinais import sinal

if(__name__ != "__main__"):
    pass
else:
    a = sinal()
    a.pede_numero()
    a.verifica_sinal()
    a.resultado()
    
    print("\n")
    print("".center(100, "@"))
    print(a.numero)
    print(a.sinal)

    print(" \neeeendddd")
