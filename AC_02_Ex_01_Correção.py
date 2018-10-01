'''
AC_02:
Exercício 01:
Objetivo: Ler um número inteiro de 3 dígitos e
imprima se o algarismo da dezena é par ou ímpar.
Entrada: Um número inteiro de no mínimo 3 dígitos
Saída: Uma msg verificando informando se a dezena do
número é par ou ímpar
'''

n=int(input("Digite um número com 3 digitos: "))

#(1) Obter a dezena do número dado
q1=n//10
resto=q1%10  #resto é a dezena do número n

# (2) Verificar se essa dezena é par ou ímpar
if resto%2==0:
    print(resto,"é par")
else:
    print(resto,"é ímpar")
