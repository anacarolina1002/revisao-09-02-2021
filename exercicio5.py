#Criação de um simulador de preço.
#A. Você deve perguntar ao cliente o preço do produto.
#B. Você deve perguntar em seguida a forma de pagamento com
#as opções a vista, a prazo sendo 1x no cartão, a prazo da loja em
#5x, a prazo da loja em 10x.
#C. A vista o produto sairá 50% a menos do valor.
#D. A prazo em 1x no cartão o produto sairá 10% a menos do valor.
#E. A prazo da loja em 5x o produto sairá 10% a mais do valor.
#F. A prazo da loja em10x o produto sairá 50% a mais do valor.
#G. Você deve mostrar ao cliente preço do produto com as taxas.
#H. As questões a prazo, você deverá mostrar também os valores
#de cada parcela.

def precoProduto():
    preco=float(input("Insira o valor do produto desejado: "))
    print("Preço do produto:",preco)
    formaPagamento=int(input('''Insira a forma de pagamento:
    1-A vista
    2-A prazo(1x no cartão)
    3-A prazo da loja(em 5x)
    4-A prazo da loja(em 10x)
    '''))
    if formaPagamento==1:
        valorDesconto=preco*(50/100)
        valorFinal=(preco-valorDesconto)
        print("O produto recebeu R$",valorDesconto,"de desconto, valor total: R$",valorFinal)
    elif formaPagamento==2:
        valorDesconto=preco*(10/100)
        valorFinal=(preco-valorDesconto)
        print("O produto recebeu R$",valorDesconto,"de desconto, valor total: R$",valorFinal)
    elif formaPagamento==3:
        valorMais=preco*(10/100)
        valorFinal=(preco+valorMais)
        valorParcela=(valorFinal/5)
        print(f'''
        O produto recebeu R$ {valorMais} de acréscimo, valor total: R${valorFinal}
        O valor de cada parcela é: {valorParcela}
        ''')
    elif formaPagamento==4:
        valorMais=preco*(50/100)
        valorFinal=(preco+valorMais)
        valorParcela=(valorFinal/10)
        print(f'''
        O produto recebeu R$ {valorMais} de acréscimo, valor total: R${valorFinal}
        O valor de cada parcela é: {valorParcela}
        ''')
precoProduto()

