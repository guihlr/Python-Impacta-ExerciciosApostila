# EXERCÍCIO 5
# Elabore um programa que determine o valor de S, em que
# S = 1/1 – 2/4 + 3/9 – 4/16 + 5/25 – 6/36 + 7/49 – 8/64 + 9/81 – 10/100. Resposta: 0.645635

# s = 0
# sinal = 1
# cadeia = ' '
# for den in range(1, 11):
#     if sinal == 1:
#         cadeia = cadeia + ' ' + str(1) + '/' + str(den)
#     else:
#         cadeia = cadeia + ' ' + str(-1) + '/' + str(den)
#
#     s = s + sinal * 1 / den
#     sinal = sinal * (-1)
# print('{:.6f}'.format(s))
# print(cadeia)
