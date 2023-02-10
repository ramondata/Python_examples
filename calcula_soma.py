#Faça um Programa que peça dois números e imprima a soma.

i=1
numeros = []
while(i <= 2):
    entrada_dados = input("Digite um numero")
    num = int(entrada_dados)
    numeros.insert(0,num)
    i+=1

soma = numeros[0] + numeros[1]
texto_saida = f"A soma dos dois numeros informados é: {soma}"
print(texto_saida.center(40,"*"))