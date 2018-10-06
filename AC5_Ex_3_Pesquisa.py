# 3) A empresa União Ltda., realizou uma pesquisa sobre a aceitação de seu produto alimentício, e necessita de um
# programa, que tabule e informe:
# è A quantidade de mulheres maiores de 20 anos indicaram o produto como bom;
# è A quantidade de mulheres maiores de 30 anos indicaram o produto como ruim;
# è A quantidade de homens que indicaram o produto como péssimo;
# è O total de homens que participaram da pesquisa.
# è O total de mulheres que participaram da pesquisa.
# As respostas foram codificadas da seguinte maneira:
# a. idade – valor numérico indicando o número de anos de vida;
# b. sexo – "masculino" para homens e "feminino" para mulheres;
# c. opinião com relação ao produto:
# 1: péssimo 2: ruim  3: regular 4: bom 5: ótimo.
# Obs.: O programa dever terminar quando o usuário digitar s (sim)

encerrar = 'n'
mulheres = 0
mulheresCom20 = 0
mulheresCom30 = 0

homens = 0
hPessimo = 0

while encerrar == 'n' or encerrar == 'N':
    idade = int(input('\nInforme sua idade: '))
    sexo = input('Informe o sexo, sendo F para Feminino ou M para Masculino: ')
    opiniao = int(input(
        'Qual é a sua opinião sobre o nosso produto:\n1: péssimo \n2: ruim  \n3: regular \n4: bom \n5: ótimo\nR:'))

    if sexo == 'F' or 'f':
        mulheres = mulheres + 1

        if idade >= 20 and opiniao == 4:
            mulheresCom20 = mulheresCom20 + 1

        if idade >= 30 and opiniao == 2:
            mulheresCom30 = mulheresCom30 + 1

    if sexo == 'M' or sexo == 'm':
        homens = homens + 1

        if opiniao == 1:
            hPessimo = hPessimo + 1

    encerrar = input('Deseja encerrar a pesquisa (S ou N)?: ')

print('\nO resultado da pesquisa é: ')
print('A quantidade de mulheres maiores de 20 anos indicaram o produto como bom é de: ', mulheresCom20)
print('A quantidade de mulheres maiores de 30 anos indicaram o produto como ruim é de: ', mulheresCom30)
print('A quantidade de homens que indicaram o produto como péssimo é de:', hPessimo)
print('\nTotal de homens que participaram da pesquisa é de: ', homens)
print('Total de mulheres que participaram da pesquisa é de: ', mulheres)
