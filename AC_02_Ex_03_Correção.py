'''
AC_2
Exercício 3: Um pescador comprou um computador
para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que
o estabelecido pelo regulamento de pesca do Estado
de SP (50 quilos), deve pagar uma multa de
R$ 4,00 por quilo excedente.
Escreva um programa que leia o peso de peixes,
e verifique se há excesso.
Se houver, determine o peso excedente e o valor da multa.
Caso contrário, mostrar “Dentro do regulamento”.

Entrada: A quantidade de peixes em kilos
Saída: Uma msg, se entra dentro ou não do regulamento.
O peso excedente e o valor da multa, se necessário.
'''

peso=float(input("Digite a qtd de peixes (kg): "))

if peso>50:
    excedente=peso-50
    multa=excedente*4
    print("Peso excedente de %.1f multa de R$ %.2f"
          %(excedente, multa))
else:
    print("Peso %.1f  dentro do regulamento" %peso)
    
