'''
Objetivo: Colocar em ordem alfabética dois nomes
Entrada: 2 strings
Saída: Os nomes em ordem alfabética
'''

nome1=input("Digite o primeiro nome: ")
nome2=input("Digite o segundo nome: ")

if nome1>nome2:
    '''trocar 2 números
    aux=nome1
    nome1=nome2
    nome2=aux
    '''
    nome1,nome2=nome2,nome1 #trocar Python

    
print(nome1,nome2)
