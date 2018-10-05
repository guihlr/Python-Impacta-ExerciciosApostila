'''
Objetivo: Encontrar o maior e o menor entre dois números
Entrada: 2 números inteiros
Saída: O maior e o menor dos números lidos
'''

n1 = int(input("Digite um número inteiro n1: "))
n2 = int(input("Digite um número inteiro n2: "))

if n1 >= n2:
    maior = n1
    menor = n2
else:
    maior = n2
    menor = n1

print("Maior = ", maior)
print("Menor = ", menor)
