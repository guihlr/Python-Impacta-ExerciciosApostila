'''
Ex 05: Cap 5
Objetivo: Escreva um programa que lê dois números inteiros e
calcula o quociente e o resto da divisão entre os números dados,
sem o uso do operador // e %
Entrada: Dois números inteiros
Saída: O quociente e o resto da divisão dos números lidos
'''
n1, n2 = input("Digite 2 números inteiros:").split(" ")
n1, n2 = int(n1), int(n2)

if n1 < n2:
    aux = n1
    n1 = n2
    n2 = aux

# Dividir n1 por n2 sem usar //. Quantidade de vezes n2 cabe no n1
cont = 0
while n2 <= n1:
    n1 = n1 - n2
    cont = cont + 1

print("Quociente da divisão = ", cont)
print("Resto da divisão = ", n1)
