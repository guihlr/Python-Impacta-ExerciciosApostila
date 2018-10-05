'''
Ex 05: Cap 5
Objetivo: Escreva um programa que lê dois números
inteiros e calcula a multiplicação entre os números dados,
sem o uso do operador *, mas sim pela soma sucessiva de um deles.
Exemplo: 3 x 4 = 3 + 3 + 3 + 3 = 4 + 4 + 4 = 12
Entrada: Dois números inteiros
Saída: A multiplicação dos números lidos
'''
n1, n2 = input("Digite 2 números inteiros:").split(" ")
n1, n2 = int(n1), int(n2)

# Multiplicar n1*n2 = somar n1 em n2 vezes
cont = 0
soma = 0
while cont < n2:
    soma = soma + n1
    cont = cont + 1

print(soma)
