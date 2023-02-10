#!/usr/bin/env python

from verifica_sexo import sexo

if(__name__ != "__main__"):
    pass
else:
    a = sexo()
    a.entrada_dados()
    a.verificador()
    a.resultado()
    
    print("")
    print("Fim")

