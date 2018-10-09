'''
Cap 6 - 7: Fatorial
Objetivo: Escreva um programa que calcule e apresente a
soma dos 20 primeiros termos da série:
100/0!+  99/1!+98/2!+  97/3!+⋯
Entrada: Um número natural
Saída: A soma dos 20 primeiros termos
'''

fatorial = 1
num = 100
F = 0
cadeia = ""
for cont in range(1, 21):
    cadeia = cadeia + " " + str(num) + "/" + str(cont - 1) + "!"
    if cont >= 2:
        fatorial = fatorial * (cont - 1)

    F = F + num / fatorial
    num = num - 1
print(F)
print(cadeia)


