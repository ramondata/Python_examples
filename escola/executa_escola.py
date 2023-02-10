#!/usr/bin/env python

import sys
import os
import escola
import aluno
import professor
from escola import escola
from professor import professor
from aluno import aluno

arg_total = sys.argv
aluno_nome = sys.argv[1]
aluno_idade = sys.argv[2]
aluno_materia_pref = sys.argv[3]
professor_nome = sys.argv[4]
professor_idade = sys.argv[5]
professor_materia_leciona = sys.argv[6]

def registra_dados():
    global arg_total
    registro = open('/home/ec2-user/escola/reg_dados.txt', 'a+')
    registro.write(f'{arg_total}\n')
    return print('dados registrados corretamente')

if(__name__ != "__main__"):
    pass
else:
    aluno_chico = aluno(aluno_nome, aluno_idade, aluno_materia_pref)
    professor_ramon = professor(professor_nome, professor_idade, professor_materia_leciona)
    
    print("visualizando atributos do aluno setados com os parametros".center(100, "@"))
    print(f'{aluno_chico.nome}')
    print(f'{aluno_chico.idade}')
    print(f'{aluno_chico.materia_preferida}')

    print('modificando os atributos do aluno com os metodos setters'.center(100, "@"))
    aluno_chico.nome = 'chico_chiquinho_chicao'
    aluno_chico.idade = 3
    aluno_chico.materia_preferida = 'carinho da mamae'

    print("visualizando atributos do aluno setados com o metodo setter".center(100, "@"))
    print(f'{aluno_chico.nome}')
    print(f'{aluno_chico.idade}')
    print(f'{aluno_chico.materia_preferida}')


    print('visualizando os atributos do professor com os parametros'.center(100, "@"))
    print(f'{professor_ramon.nome}')
    print(f'{professor_ramon.idade}')
    print(f'{professor_ramon.materia_leciona}')
    
    print('modificando os atributos dos professores com os metodos setters'.center(100, "@"))
    professor_ramon.nome = 'Ramão'
    professor_ramon.idade = 29
    professor_ramon.materia_leciona = 'Pyyyyyythoooon'

    print('visualizando os atributos do professor setados com o metodo setter'.center(100, "@"))
    print(f'{professor_ramon.nome}')
    print(f'{professor_ramon.idade}')
    print(f'{professor_ramon.materia_leciona}')

    print(f'{aluno_chico.nome_da_classe()}')
    print(f'{professor_ramon.nome_da_classe()}')

    print(f'{aluno_chico.direito_autoral()}')
    print(f'{professor_ramon.direito_autoral()}')

    sys.stdout.write('\n')
    sys.stdout.write(f'{arg_total}\n')
    sys.stdout.write('fim\n')

    registra_dados()
