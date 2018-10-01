'''
Exercício 06:
Objetivo: Calcular a conta da água e a conta com desconto de 15%
Entrada: salário mínimo e a qtd consumida de água
Saída: Valores dos dados lidos
'''

salario=float(input("Digite o valor do salário mínimo: "))
qtdAgua=float(input("Digite a qtd de água consumida: "))

valorLitro=0.02*salario/1000
contaAgua=valorLitro*qtdAgua

print("O valor da conta de água mensal = R$ %.2f" %contaAgua)
