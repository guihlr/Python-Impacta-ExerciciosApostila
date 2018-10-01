'''
Objetivo: Veirificar se um número é divisível por 3 e
por 5 ao mesmo tempo.
Entrada: Um número inteiro
Saída: Uma msg informando se é divisível por 3 e 5
'''

n=int(input("Digite um número inteiro: "))
if n%3==0 and n%5==0:
    msg="É divisível por 3 e 5"
else:
    msg="NÃO é divisível por 3 e 5"

print(n, msg)
