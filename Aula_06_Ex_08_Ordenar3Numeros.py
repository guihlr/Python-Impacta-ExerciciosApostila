'''
Objetivo: Colocar em ordem crescente 3 números
Entrada: 3 números inteiros
Saída: Os 3 números lidos em ordem crescente
'''

a=int(input("Digite o 1o. número: "))
b=int(input("Digite o 2o. número: "))
c=int(input("Digite o 3o. número: "))

#Colocar em a o menor de todos os números
if a>b or a>c:
    if b<c:
        #Trocar(a,b)
        aux=a
        a=b
        b=aux
    else:
        #Trocar(a,c)
        aux=a
        a=c
        c=aux
#Colocar em b o intermediario e em c o maior
if b>c:
    #Trocar(b,c)
    aux=b
    b=c
    c=aux

print(a,b,c)
