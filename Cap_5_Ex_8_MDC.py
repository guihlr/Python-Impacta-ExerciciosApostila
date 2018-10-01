'''
Objetivo: Escreva um programa que calcule o MDC (máximo divisor comum)
entre dois números naturais.
Entrada: 2 números inteiros e positivos
Saída: O MDC entre os números lidos
'''

#Lendo dos dados de entrada
n1=-1
n2=-1
while n1<=0 or n2<=0:
    n1=int(input("Digite um número inteiro e positivo n1: "))
    n2=int(input("Digite um número inteiro e positivo n2: "))

resto=1
while resto!=0:
    resto=n1%n2
    n1=n2       #atualização
    n2=resto    #atualização

print(n1)
    
