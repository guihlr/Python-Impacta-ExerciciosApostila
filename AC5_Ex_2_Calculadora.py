# 2) Faça um programa que mostre um menu para o usuário escolher uma operação ou sair do programa. Por exemplo:
# Soma .................... +
# Subtração ............. -
# Multiplicação......... *
# Divisão................... /
# Sair ....................... 0
# O programa deve reconhecer a opção escolhida pelo usuário e solicitar a entrada de dois números caso a opção escolhida
# seja uma das operações. Depois de fazer a operação e mostrar o resultado o programa deve continuar em execução para
# que o usuário faça selecione operação e outros números. O programa só terminará caso o usuário digite 0.

from time import sleep

while True:
    print("""
1 - Soma
2 - Subtração
3 - Multiplicação
4 - Divisão
5 - Sair 
""")
    opcao = int(input('Escolha uma Opção: '))
    if opcao == 5:
        break
    elif opcao == 1:
        n1 = float(input('Digite o primeiro número para ser somado: '))
        n2 = float(input('Digite o segundo número para ser somado: '))
        resultado = n1 + n2
        print('-=-' * 15)
        print('CALCULANDO...')
        print('-=-' * 15)
        sleep(2)
        print('\nO resultado da soma é {:.2f}'.format(resultado))

    elif opcao == 2:
        n1 = float(input('Digite o primeiro número a ser subtraido: '))
        n2 = float(input('Digite o segundo número a ser subtraido: '))
        resultado = n1 - n2
        print('-=-' * 15)
        print('CALCULANDO...')
        print('-=-' * 15)
        sleep(2)
        print('\nO resultado da subtração é {:.2f}'.format(resultado))

    elif opcao == 3:
        n1 = float(input('Digite o primeiro número a ser multiplicado: '))
        n2 = float(input('Digite o segundo número a ser multiplicado: '))
        resultado = n1 * n2
        print('-=-' * 15)
        print('CALCULANDO...')
        print('-=-' * 15)
        sleep(2)
        print('\nO resultado da multiplicação é {:.2f}'.format(resultado))

    elif opcao == 4:
        n1 = float(input('Digite o primeiro número a ser dividido: '))
        n2 = float(input('Digite o segundo número a ser divido: '))
        resultado = n1 / n2
        print('-=-' * 15)
        print('CALCULANDO...')
        print('-=-' * 15)
        sleep(2)
        print('\nO resultado da divisão é {:.2f}'.format(resultado))

    else:
        print('*-*'*10)
        print('Opção Inválida!')
        print('*-*' * 10)
