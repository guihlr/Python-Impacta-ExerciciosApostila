'''
Cap 6 - Ex 4: Série H
Objetivo: Escreva um programa  que calcule o valor de H,
sendo que ele é determinado pela série
H = 1/1 + 3/2 + 7/4 + 11/6 + 15/8 + 19/10 + … + 99/50.
Entrada: Nenhuma
Saída: A soma dos termos
'''

H=1
num=3
cadeia="1/1"
for den in range(2,51,2):
    cadeia=cadeia+ " " + str(num)+"/"+str(den)
    H=H+num/den
    num=num+4

print(H)
print(cadeia)


