'''
Objetivo: Leia um número inteiro de 3 dígitos,
determine e apresente o número invertido
Entrada: Um número de 3 dígitos
Saída: O número lido invertido
'''

n=int(input("Digite um número de 3 dígitos:"))
r1=n%10
q1=n//10
r2=q1%10
q2=q1//10
n_inv=r1*100+r2*10+q2
print(n_inv)


