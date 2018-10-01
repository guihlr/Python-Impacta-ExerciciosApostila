'''
Objetivo: Calcular a média semestral
Entrada: Média de ACs, nota da prova e frequencia
Saída: Média e msg se aprovado sem SUB, aprovado com SUB,
reprovado por nota e reprovado por frequencia
'''
ACs=float(input("Digite a média das ACs:"))
prova=float(input("Digite a nota da prova:"))
faltas=float(input("Digite o número de faltas:"))

media=(ACs*6 + prova*4)/10
print("Média parcial = %.2f" %media)

if media>=6.0 and faltas<=20:
    print("Aprovado sem SUB com média = %.2f" %media)
else:
    sub=float(input("Digite a nota da Substitutiva:"))
    mediaF=(ACs*6 + sub*4)/10
    if mediaF>=6.0 and faltas<=20:
        print("Aprovado com SUB com média final = %.2f" %mediaF)
    else:
        print("Reprovado")


        

