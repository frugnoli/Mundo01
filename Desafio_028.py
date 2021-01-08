# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o
# usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar . . .")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? "))
print("-=-" * 20)
listas = [0, 1, 2, 3, 4, 5]
computador = randint(0, 5)
if jogador in listas:
    print("PROCESSANDO . . .")
    sleep(2)
    if jogador == computador:
        print("PARABÉNS! Você conseguiu me vencer!")
    else:
        print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))
else:
    print("Números tem que ser de 0 a 5, tente novamente!")

