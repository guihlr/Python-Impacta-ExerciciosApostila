'''
Objetivo: Verificar se um ano é bissexto.
400 em 400 anos é bissexto, mas de 100 em 100 anos,
não é bissexto
Feitas as correções de calendário definiu-se a nova regra para o cálculo dos anos bissextos:

De 4 em 4 anos é ano bissexto.
De 100 em 100 anos não é ano bissexto.
De 400 em 400 anos é ano bissexto.
Prevalecem as últimas regras sobre as primeiras.

Entrada: Um número inteiro
Saída: Uma msg informando se é ou não bissexto
'''

ano=int(input("Digite um número inteiro: "))
if (ano%4==0) and (not(ano%100==0)or(ano%400==0)):
    msg="É bissexto"
else:
    msg="NÃO é bissexto"

print(ano, msg)
