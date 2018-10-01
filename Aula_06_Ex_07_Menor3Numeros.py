'''
Objetivo: Encontrar o menor de 3 numeros
Entrada: 3 números
Saída: o menor
'''

a=int(input("Digite um número a:"))
b=int(input("Digite um número b:"))
c=int(input("Digite um número c:"))

if a<b and a<c:
    menor=a
else:
    if b<c:
        menor=b
    else:
        menor=c
        
print(menor)
