'''
Cap 6 - Ex 4: Série H
Objetivo: Elabore um programa que determine o valor de S,
em que
S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + 7/49 – 8/64 + 9/81 – 10/100.
Entrada: Nenhuma
Saída: A soma dos termos
'''

S=0
sinal=1
cadeia=" "
for den in range(1,11):
    if sinal==1:
        cadeia=cadeia + "  " + str(1)+"/"+str(den)
    else:
        cadeia=cadeia + "  " + str(-1)+"/"+str(den)
    S=S+sinal*1/den
    sinal=sinal*(-1)

print(S)
print(cadeia)


