'''
Objetivo: Elabore um programa que verifica se um número natural
é primo.
Entrada: Um número inteiro e positivo
Saída: Uma msg se é primo ou não
'''

n = -1
while n <= 0:
    n = int(input('Digite um número inteiro e positivo: '))

ndiv = 0
for cont in range(1, n + 1):
    resto = n % cont
    if resto == 0:
        ndiv = ndiv + 1

if ndiv <= 2:
    print('{} É PRIMO'.format(n))
else:
    print('{} NÃO É PRIMO'.format(n))
