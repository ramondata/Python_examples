#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato,
#faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

class financas:

    def __init__(self):
        self.valor_hora = 0.0
        self.total_horas = 0.0
        self.salario_bruto = 0.0
        self.salario_liquido = 0.0
        self.desconto_inss = 0.0
        self.desconto_sindicato = 0.0
        self.desconto_ir
        
    def recebe_dados(self):
        dado = float(input("Quanto vc ganha por hora? \n"))
        self.valor_hora = dado
        dados = float(input("Quantas horas vc trabalhou? \n"))
        self.total_horas = dados
        return (self.valor_hora, self.total_horas)
    
    def calcula_salario_bruto(self):
        self.salario_bruto = self.valor_hora * self.total_horas
        return self.salario_bruto
        
    def calcula_descontos(self):
        self.desconto_inss = self.salario_bruto * 0.08
        self.desconto_ir = self.salario_bruto * 0.11
        self.desconto_sindicato = self.salario_bruto * 0.05
        return (self.desconto_inss, self.desconto_ir, self.desconto_sindicato)
    
    def calcula_salario_liquido(self):
        self.salario_liquido = self.calcula_salario_bruto() - self.desconto_inss - self.desconto_ir - self.desconto_sindicato
        return self.salario_liquido
        
import fin
from fin import financas

if (__name__ != "__main__"):
    pass
else:
    a = financas()
    a.recebe_dados()
    a.calcula_salario_bruto()
    a.calcula_descontos()
    a.calcula_salario_liquido()