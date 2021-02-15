#Criação de um simulador de caixa eletrônico.
#A. Você deve perguntar ao usuário qual será o valor para
#ser sacado (Apenas números inteiros)
#B. O programa deve informar quantas cédulas de cada
#valor deverá ser entregue ao usuário
#C. As cédulas deveram ser nos valores de R$50, R$20, R$
#10 e R$ 1.
#D. Devem também fazer na letra A as verificações de erros
#possíveis.
def cedulasDisponiveis():
    nome=(input("Insira seu nome: "))
    valorSaque=int(input(f'''Olá,{nome}
    Bem-vindo(a) ao Banco Moeda Mundial. 
    Insira o valor a ser sacado
    >'''))
    total=valorSaque
    cedula=50
    totalCedulas=0
    while True:
        if valorSaque>=cedula:#valor do saque for maior q 50
            valorSaque-=cedula#tira o valor de 50 sempre q der
            totalCedulas+=1#o numero de cedulas sobe a cada 50 que é tirado do valor de saque
        else:
            if totalCedulas>0:
                print(f'''Total de {totalCedulas} de cedulas de R${cedula},00''')  
            elif cedula==50:
                cedula=20
            elif cedula==20:
                cedula=10
            elif cedula==10:
                cedula=1
            totalCedulas=0
            SystemExit
cedulasDisponiveis()
