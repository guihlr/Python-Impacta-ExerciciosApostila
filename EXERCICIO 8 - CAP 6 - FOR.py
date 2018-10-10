# Elabore um programa que verifica se um número natural é primo.

# num = int(input('Digite um número: '))
# total = 0
# for cont in range(1, num + 1):
#     if num % cont == 0:
#         print('\033[33m', end='')
#         total = total + 1
#     else:
#         print('\033[31m', end='')
#     print('{} '.format(cont), end='')
# print('\n\033[mO número {} foi divisível {} vezes'.format(num, total))
# if total == 2:
#     print('ele é primo')
# else:
#     print('ele não é primo')

num = int(input('Digite um número: '))
cont = 1
for cont in range(1, num):
    if num % 2 == 1:
        cont = cont + 1
        print('É PRIMO!')
        break
    else:
        print('NÃO É PRIMO!')
        break
