#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

i = 0
id_notas = ['nota1', 'nota2', 'nota3', 'nota4']
notas = []
while(i < 4):
    entrada_dados = input(f'Digite a {id_notas[i]}')
    num = float(entrada_dados)
    notas.insert(0,num)
    i+=1
    
soma = round(sum(notas), 2)

media = round(soma/len(notas), 2)

texto_saida = f"A soma acumuluda de notas foi {soma} e a media final foi {media}".center(40, "*")
print(texto_saida)