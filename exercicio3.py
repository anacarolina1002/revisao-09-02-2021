#Crie um programa que receba varias notas onde o
#programa irá retornar um dicionário com as informações:
#A. Quantidade de notas;
#B. A maior nota;
#C. A menor nota;
#D. A média da turma;
#E. A situação do aluno.
dicionarioNotas={6,5,2,3,7.3,8.1,7.5,10,9.6}
numNotas={}
media={}
notaMaior={}
notaMenor={}
def quantidade(dicionarioNotas):
    global numNotas
    numNotas=(len(dicionarioNotas))
    maiorNota(dicionarioNotas)  
def maiorNota(dicionarioNotas):
    global notaMaior
    notaMaior=max(dicionarioNotas,key=float)
    menorNota(dicionarioNotas)
def menorNota(dicionarioNotas):
    global notaMenor
    notaMenor=min(dicionarioNotas,key=float)
    mediaTurma(dicionarioNotas)
def mediaTurma(dicionarioNotas):
    global media
    somaNumeros=sum(dicionarioNotas)
    media=somaNumeros/numNotas
    situacaoAluno(dicionarioNotas)
def situacaoAluno(dicionarioNotas): 
    if media<7:
        print(f'''
        Quantidade de notas:{numNotas}
        Maior nota da turma:{notaMaior}
        Menor nota da turma:{notaMenor}
        Média da turma:{media}
        Alunos não foram aprovados! Média necessária igual à 7.''')
        SystemExit
    else:
        print(f'''
        Quantidade de notas:{numNotas}
        Maior nota da turma:{maiorNota}
        Menor nota da turma:{menorNota}
        Média da turma:{media}
        Alunos foram aprovados! Média necessária igual à 7.''')
        SystemExit
quantidade(dicionarioNotas)