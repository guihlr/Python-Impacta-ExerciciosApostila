mes = 1
ano = 1
dia = 1
diaSemana = " "

while mes > 0 or dia > 0 or ano > 0:

    dia = int(input("Insira o dia desejado: "))
    mes = int(input("Insira o mes desejado: "))
    ano = int(input("Insira o ano desejado: "))
    seculo = ano // 100
    digitoAno = ano % 100
    valor = digitoAno + (digitoAno // 4)
    bissexto = False

    if seculo == 18:
        valor = valor + 2
    elif seculo == 20:
        valor = valor + 6

    if (ano % 4 == 0) and (not (ano % 100 == 0) or (ano % 400 == 0)):
        print("Ano bissexto")
        print("Digite -1 para parar")
        bissexto = True
    else:
        print("Não bissexto")
        print("Digite -1 para parar")
        bissexto = False

    if mes == 1 and bissexto == False:
        valor = valor + 4

    elif mes == 2 and bissexto == True:
        valor = valor + 3

    elif bissexto == False and mes == 2:
        valor = valor + 4

    elif mes == 3 and mes == 11:
        valor = valor + 4

    elif mes == 4 and mes == 7:
        valor = valor + 0

    elif mes == 5:
        valor = valor + 2

    elif mes == 6:
        valor = valor + 5

    elif mes == 8:
        valor = valor + 3

    elif mes == 10:
        valor = valor + 1

    else:
        valor = valor + 6

    valor = (valor + dia) % 7

    if valor == 1:
        diaSemana = "Domingo"
    elif valor == 2:
        diaSemana = "Segunda"
    elif valor == 3:
        diaSemana = "Terça"
    elif valor == 4:
        diaSemana = "Quarta"
    elif valor == 5:
        diaSemana = "Quinta"
    elif valor == 6:
        diaSemana = "Sexta"
    else:
        diaSemana = "Sábado"

    print("%i de %i de %i é %s" % (dia, mes, ano, diaSemana))
