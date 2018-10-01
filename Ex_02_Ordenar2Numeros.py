'''
Objetivo: Colocar em ordem crescente dois números
Entrada: 2 números inteiros
Saída: Os números lidos em ordem crescente
'''

n1=int(input("Digite um número inteiro n1: "))
n2=int(input("Digite um número inteiro n2: "))

if n1>n2:
    '''trocar 2 números
    aux=n1
    n1=n2
    n2=aux
    '''
    n1,n2=n2,n1 #trocar Python

    
print(n1,n2)
