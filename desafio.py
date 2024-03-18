"""
    Crie um jogo de "joken pò", ou seja "pedra, papel, e tesoura".

    Pergunte para o jogador 1 qual da opções ele vai querer
    Pergunte para o jogador 2 qual da opções ele vai querer
    Dependendo do resultado, o jogo dirá "Jogador 1 venceu", "Jogador 2 venceu" ou "empate"
"""
from time import sleep
from random import randint

itens = ("Pedra", "Papel", "Tesoura")
jogador1 = randint(0, 2)

print("\033[1;35mBem vindo ao Jogo Jokenpô, que os jogos comecem.. iniciem suas jogadas!!!\033[m")

print('''Suas opções:
      [0] Pedra
      [1] Papel
      [2] Tesoura
      ''')


# Para garantir que o programa continue, o laço de repetição pedirá ao jogador que faça uma escolha válida até que digite um número de 0 a 2.
while True:
    jogador2 = int(input("Qual é a sua escolha? "))
    if jogador2 in [0, 1, 2]:
        break
    else:
        print("\033[1;31mEscolha inválida! Por favor, escolha um número entre 0 e 2.\033[m]")

# ESCREVENDO JOKENPO...
print("-*" * 25)

print('\033[1;36mJO')
sleep(1)
print('KEN')
sleep(1)
print("PÔ!!!\033[m")
sleep(2)

print("-*" * 25)

print(f"Jogador 1 escolheu {itens[jogador1]}")
print(f"Jogador 2 escolheu {itens[jogador2]}")
print("-=" * 25)

# Se os dois jogadores escolherem a mesma opção
if jogador1 == jogador2:
    print("\033[0;33mEMPATE\033[m")
    # Se diante a essas escolhas o jogador1 escolher PEDRA e jogador2 TESOURA, 
    # ou jogador1 escolher PAPEL e jogador2 PEDRA,
    # ou jogador1 escolher TESOURA e jogador2 PAPEL..
    # O JOGADOR 1 VENCE!
elif (jogador1 == 0 and jogador2 == 2) or (jogador1 == 1 and jogador2 == 0) or (jogador1 == 2 and jogador2 == 1):
    print("\033[1;32mJOGADOR 1 VENCEU.\033[m")
    # senão...
    # JOGADOR 2 VENCE!
else:
    print("\033[1;32mJOGADOR 2 VENCEU.\033[m")
