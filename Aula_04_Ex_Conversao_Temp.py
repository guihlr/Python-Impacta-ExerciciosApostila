'''
Exercício 3 do Cap 3:
Objetivo: Dada a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius,
sabendo que:  
c =  5*(f-32)/9
Entrada: A temperatura em Fahrenheit
Saída: a temperatura correspondente em Celsius
'''

f=float(input("Digite a temperatura em Fahrenheit: "))
c=5*(f-32)/9
print("%.2f Fahrenheit ==> %.2f Celsius" %(f,c))
