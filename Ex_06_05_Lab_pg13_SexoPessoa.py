'''
Objetivo: Ler do teclado o sexo de uma pessoa.
Se o sexo digitado for “M” ou “m” ou “F” ou “f”,
escrever na tela “Sexo válido!”.
Caso contrário, exibir “Sexo inválido!”.

Entrada: Um caracter
Saída: Uma msg informando se é ou não válido
'''

sexo=input("Digite um número inteiro: ")
s=sexo.upper()
#if sexo=="M"or sexo=="m" or sexo=="F" or sexo=="f":
if s=="M" or s=="F":
    msg="É válido"
else:
    msg="NÃO é válido"

print(sexo,msg)
