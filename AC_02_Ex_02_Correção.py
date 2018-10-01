'''
AC_02
Exercício 02: Ler notas de três avaliações de um aluno.
A primeira avaliação tem peso 2, a segunda tem peso 3
e, a terceira, peso 5.
Calcule a média do aluno. Se a média do aluno for maior
ou igual a 6, o aluno está aprovado; caso contrário,
o aluno está reprovado.
Mostre o resultado da decisão.
Entrada: 3 notas
Saída: Média e msg de aprovado ou reprovado
'''

nota1=float(input("Digite a nota1: "))
nota2=float(input("Digite a nota2: "))
nota3=float(input("Digite a nota3: "))

media=(nota1*2+nota2*3+nota3*5)/10

if media >=6.0:
    print("A média = %.2f,aluno Aprovado!" %media)
else:
    print("A média = %.2f,aluno REprovado!" %media)

