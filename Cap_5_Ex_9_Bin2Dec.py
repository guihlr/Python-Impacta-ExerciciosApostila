'''
Objetivo: Escreva um programa que leia um número inteiro e positivo
representando um número binário,determine o seu equivalente decimal. 
Entrada: Um número inteiro e positivo, representando um binário
Saída: o correspondente em binário
'''

#Lendo dos dados de entrada
binario=-1
while binario<=0:
    binario=int(input("Digite um número inteiro e positivo binário: "))

decimal=0
cont=0
while binario!=0:
    resto=binario%10
    decimal=decimal + resto*2**cont
    cont=cont+1         #atualização
    binario=binario//10 #atualização

print(decimal)
