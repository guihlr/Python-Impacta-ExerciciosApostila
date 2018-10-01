'''
Objetivo: Calcular as raízes da eq do 2o. grau, se existirem
Entrada: 3 números reais, representando os coeficientes da equação
Saída: Uma msg informando que é não polinômio de grau 2, ou não existe
raízes reais ou as raízes
ax^2 + bx + c = 0
'''

import math

a=float(input("Digite o coeficiente a (a<>0): "))
b=float(input("Digite o coeficiente b: "))
c=float(input("Digite o coeficiente c: "))

if a==0:
    print("Não é equaçao do 2o. grau")
else:
    delta=b*b-4*a*c
    if delta<0:
        print("Não possui raízes reais")
    else:
        if delta==0:
            x=-b/(2*a)
            print("Uma única raíz = %.2f" %x)
        else:
            x1=(-b + math.sqrt(delta))/(2*a)
            x2=(-b - math.sqrt(delta))/(2*a)
            print("x1=%.2f e x2=%.2f" %(x1,x2))


