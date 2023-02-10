#Faça um Programa que converta metros para centímetros.
# 1 metro = 100 centimetros

medida_metro = input("Qual medida em metros deseja converter a centimetros? \n")
medida_num = round(float(medida_metro), 2)
conversor = round(medida_num*100, 2)
texto_saida = f"A medida de {medida_num} metros, equivale a {conversor} centimetros".center(100, "*")
print(texto_saida)