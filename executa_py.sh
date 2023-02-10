#!/usr/bin/env bash

echo $(clear)

echo '###############################################################################'
echo '########### Direcionador de arquivo python para execução automática ###########'
echo '###############################################################################'
echo
echo 'Escolha seu programa de acordo com a lista abaixo: '
echo
echo $(ls)

read -p "Digite o nome do programa escolhido" prog

python $prog

