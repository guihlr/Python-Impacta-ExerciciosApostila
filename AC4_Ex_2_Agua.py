'''
Objetivo: Escreva um programa que, dado o consumo de uma residência em m3 ,
calcula o valor da conta de água daquela residência.
Entrada: A única linha da entrada contém um único inteiro N, indicando o consumo de água
da residência, em m³ (0 ≤ N ≤ 10³).
Saída: Seu programa deve imprimir uma única linha, contendo o valor da conta de
água daquela residência.
'''

n=int(input("Digite o consumo de água (m3): "))

if n<=10:
    valorConta=7
elif n<=30:
    valorConta=(n-10)+ 7
elif n<=100:
    valorConta=(n-30)*2 + 27
else:
    valorConta=(n-100)*5 + 167

print("O valor da conta = R$ %.2f" %valorConta)
    

