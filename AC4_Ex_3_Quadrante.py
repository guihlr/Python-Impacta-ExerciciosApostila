'''
Objetivo: Leia 2 valores com uma casa decimal (x e y), que devem representar as
coordenadas de um ponto em um plano.
Entrada: As coordenadas do ponto P=(x,y)
Saída: A saída deve apresentar o quadrante em que o ponto se encontra.
'''

x=float(input("Digite o ordenada x do ponto P=(x,y): "))
y=float(input("Digite o ordenada y do ponto P=(x,y): "))

if x==0 and y==0:
    print("Origem")
elif x==0 and y!=0:
    print("Eixo Y")
elif x!=0 and y==0:
    print("Eixo X")
elif x>0 and y>0:
    print("Q1")
elif x<0 and y>0:
    print("Q2")
elif x<0 and y<0:
    print("Q3")
else:
    print("Q4")
    

