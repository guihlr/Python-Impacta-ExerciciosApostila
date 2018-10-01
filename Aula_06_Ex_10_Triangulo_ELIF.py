'''
Objetivo: Verificar se 3 números foram triangulo, se formar, fazer
a classificação
Entrada: 3 números reais, representando os lados de um triangulo
Saída: Msg informando que não forma triangulo ou a classificação em:
equilatero, isosceles ou escaleno
'''

a=float(input("Digite o lado a: "))
b=float(input("Digite o lado b: "))
c=float(input("Digite o lado c: "))

if a<b+c and b<a+c and c<a+b:
    if a==b and b==c:
        print("Triângulo equilátero")
    elif a==b or b==c or a==c:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
            
else:
    print("Não forma triângulo")
    


