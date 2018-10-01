'''
Objetivo: Calcular a distância entre 2 pontos
Entrada: Dois pontos P1=(x1,y1) e P2=(x2,y2)
Saída: a distância entre os pontos dados
'''
import math

x1=float(input("Digite a ordenada x1 de P1=(x1,y1):"))
y1=float(input("Digite a ordenada y1 de P1=(x1,y1):"))
x2=float(input("Digite a ordenada x2 de P2=(x2,y2):"))
y2=float(input("Digite a ordenada y2 de P2=(x2,y2):"))

d=math.sqrt((x2-x1)**2+(y2-y1)**2)

print(d)


