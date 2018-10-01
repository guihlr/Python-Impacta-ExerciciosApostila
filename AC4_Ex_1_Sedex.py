'''
Objetivo: Escreva um programa que, dado o diâmetro de uma bola e
as 3 dimensões de uma caixa (altura, largura e profundidade),
diz se a bola de boliche cabe dentro da caixa ou não.
Entrada: A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 10.000)
que indica o diâmetro da bola de boliche.
A segunda linha da entrada contém 3 números inteiros separados
por um espaço cada: a altura A (1 ≤ A ≤ 10.000),
seguida da largura L (1 ≤ L ≤ 10.000) e
da profundidade P (1 ≤ P ≤ 10.000).
Saída: Seu programa deve imprimir uma única linha, contendo a letra 'S'
caso a bola de boliche caiba dentro da caixa ou 'N' caso contrário
'''

n=int(input("Digite o diâmetro inteiro da bola: "))

a,l,p=input("Digite a altura,largura e profundidade da bola(a l p): ").split(' ')
a,l,p=int(a),int(l),int(p)

if n<=a and n<=l and n<=p:
    print ('S')
else:
    print('N')
    

