'''
Escreva um programa que que calcule o MMC (mínimo múltiplo comum) entre dois números
naturais
Entrada: 2 numeros naturais
Sai´da: O MMC entre os números lidos
'''

#Lê 2 numeros inteiros e positivos
n1=-1
n2=-1
while n1<=0 or n2<=0:
    n1=int(input("Digite um número inteiro e positivo n1: "))
    n2=int(input("Digite um número inteiro e positivo n2: "))

aux=n1
resto=n1%n2
while resto!=0:
    aux=aux+n1 #multiplos de n1
    resto=aux%n2

print(aux)
