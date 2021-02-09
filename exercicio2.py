#Crie um programa mais precisamente um jogo que faça o computador 
#jogar com você pedra, papel ou tesoura

from random import randint
import time
jogadas=["Pedra","Papel","Tesoura"]
respComputador=randint(0,2)
nome=input("Insira seu nome:")
respJogador=int(input(f'''Olá, jogador(a) {nome}! Escolha uma das opções abaixo:
0-Pedra
1-Papel
2-Tesoura
>'''))
print("JO")
time.sleep(2)
print("QUEM")
time.sleep(2)
print("PO!")
time.sleep(2)
print(nome,"escolheu:",jogadas[respJogador])
print("Computador escolheu:",jogadas[respComputador])

if respJogador==0 and respComputador==2:
    print("Parabéns,",nome,"você venceu o computador!")
elif respComputador==0 and respJogador==2:
    print("Que pena! Você perdeu.")
if respJogador==1 and respComputador==0:
    print("Parabéns,",nome,"você venceu o computador!")
elif respComputador==1 and respJogador==0:
    print("Que pena! Você perdeu.")
if respJogador==2 and respComputador==1:
    print("Parabéns,",nome,"você venceu o computador!")
elif respComputador==2 and respJogador==1:
    print("Que pena! Você perdeu.")
if respComputador==respJogador:
    print("Empate!")


