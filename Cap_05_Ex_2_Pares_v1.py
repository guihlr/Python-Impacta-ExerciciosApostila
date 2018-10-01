'''
Objetivo: Exibir os pares de 0 até o numero informado
pelo usuário
Entrada: Um número inteiro
Saída: Os pares até o número dado
'''

n=int(input("Digite um número inteiro: "))
cont=0
while cont<=n:
    if cont%2==0:
        print(cont)
    cont=cont+1

