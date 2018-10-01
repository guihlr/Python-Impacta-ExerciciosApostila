'''
Turma: ADS-1A = LP1 - 22/08
Ana Cristina

Objetivo: Calcular a hipotenusa de um triangulo retangulo
Entrada: Dois números inteiros
Saída: Um número inteiro
'''
import math

a=int(input("Digite o comprimento do lado a: "))
b=int(input("Digite o comprimento do lado b: "))

hip=math.sqrt(a*a + b*b)

print(hip)


