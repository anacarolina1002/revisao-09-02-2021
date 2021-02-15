#Crie um programa que receba um numero inteiro de 1 ao 10 e imprima sua tabuada.
def numeros():
    multiplicando=int(input("Insira um número para que sua tabuada seja exibida: "))
    for multiplicador in range(11):
        resultado=multiplicando*multiplicador
        print(multiplicando,"X",multiplicador,"=",resultado)
numeros()