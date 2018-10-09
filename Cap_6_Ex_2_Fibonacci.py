'''
Cap 6 - Ex 2: Série de Fibonacci
Objetivo: Escreva um programa que apresente a
série de Fibonacci até o n-ésimo termo (n > 0).
Entrada: Um número inteiro e positivo
Saída: O n-ésimo termo
'''

n = -1
while n <= 0:
    n = int(input("Digite o termo da série que deseja obter"))

post = 0
ant = 1
atual = 1
for cont in range(n - 1):
    print(atual)
    atual = ant + post
    post = ant  # atualização
    ant = atual  # atualização

print("O %d-ésimo termo = %d" % (n, atual))

