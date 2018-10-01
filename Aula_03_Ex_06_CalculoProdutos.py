'''
Exercício 06:
Objetivo: Escreva um programa que mostre os valore
que armazenam fruta, verdura e legume
Entrada: Uma fruta, uma verdura, um legume
Saída: Valores dos dados lidos
'''

fruta=input("Digite o nome de uma fruta: ")
valorFruta=float(input("Digite o valor unitário da %s: " %fruta))
verdura=input("Digite o nome de uma verdura: ")
valorVerdura=float(input("Digite o valor unitário da %s: " %verdura))
legume=input("Digite o nome de um legume: ")
valorLegume=float(input("Digite o valor unitário do %s: " %legume))

print(fruta,":",valorFruta)
print(verdura,":",valorVerdura)
print(legume,":",valorLegume)
