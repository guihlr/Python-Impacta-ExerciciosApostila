'''
Cap 02: Ex (2):
Objetivo:Trocar os valores de dois números inteiros
Entrada: Dois números inteiros n1 e n2
Saída: Os números lidos com valores trocados.
'''

n1=int(input("Digite um número inteiro n1:"))
n2=int(input("Digite um número inteiro n2:"))


aux=n1
n1=n2
n2=aux

#n1,n2=n2,n1

print("n1=%d n2=%d" %(n1,n2))
