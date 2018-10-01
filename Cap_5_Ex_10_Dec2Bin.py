'''
Objetivo: Escreva um programa que Escreva um programa que leia um número inteiro e positivo representando um número decimal,
determine o seu equivalente binário. 
Entrada: 1 número inteiro e positivo
Saída: o correspondente em binário
'''

#Lendo dos dados de entrada
decimal=-1
while decimal<=0:
    decimal=int(input("Digite um número inteiro e positivo decimal: "))

binario=0
cont=0
while decimal !=0:
    resto=decimal%2
    binario=binario + resto*10**cont
    cont=cont+1         #atualização
    decimal=decimal//2 #atualização

print(binario)
