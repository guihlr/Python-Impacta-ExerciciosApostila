# 1) Escreva um programa que leia uma sequência de números inteiros, encontre e imprima o maior e o menor número.
# A entrada de um número negativo indica que sequência terminou.

num = int(input('Digite um número inteiro: '))
maior = num
menor = num
while num > -1:
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    num = int(input('Digite outro número inteiro : '))

print('\nO maior número é {}\nO menor número é {}'.format(maior, menor))
