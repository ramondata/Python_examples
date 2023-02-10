#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from vogal_ou_consoante import letra

if(__name__ != "__main__"):
    pass
else:
    for i in range(1,11,1):
        a = letra()
        a.entrada_dados()
        a.verificador()
        a.resultado()
    print('é isso, mais nada, acabou, orrevuá')
