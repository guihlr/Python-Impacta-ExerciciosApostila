'''
Exercício 03:
Objetivo: Escreva um programa que receba o salário de um funcionário
e o percentual de aumento a ser aplicado. Calcule e apresente o valor
do aumento.
Entrada: Salario e percentual de aumento
Saída: Valor do aumento
'''

salario=float(input("Digite o seu salario: "))
percAumento=float(input("Digite o percentual de aumento: "))

aumento=salario*percAumento/100

print("O aumento será de R$ %.2f" %aumento)
