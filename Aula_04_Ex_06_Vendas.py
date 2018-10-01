'''
6 (b)
'''

produto=float(input("Digite o valor do produto:"))

if produto<=20.0:
    venda=produto+45/100*produto
else:
    venda=produto+30/100*produto

print("%.2f será vendido por %.2f" %(produto,venda))


