'''
Objetivo: Num determinado Estado, para transferências
de veículos, o DETRAN cobra uma taxa de 2,5% para
carros fabricados antes de 2010 e uma taxa de 3,5%
para os fabricados de 2010 em diante, taxa esta
incidindo sobre o valor de tabela do carro.
Escreva um programa lê o ano e o preço do carro
e a seguir calcula e imprime a taxa a ser paga.

Entrada: O ano do carro e o preço
Saída: A taxa do Detran
'''

ano=int(input("Digite o ano do carro: "))
preco=float(input("Digite o preço do carro: "))

if ano<2010:
    taxa=0.025*preco
else:
    taxa=0.035*preco

print("R$ %.2f" %taxa)
