"""
Crie um programa que faça o computador jogar jokenpô com você
"""
import os 
import random
import time

print('=' * 5,'Bem-vindo ao Jokenpô!','=' * 5)
inicio = input('Vamos começar?\n[s/n]: ').lower()

itens = ('pedra', 'papel', 'tesoura')
lista = random.choice(['pedra', 'papel', 'tesoura'])

if inicio == 's':
    os.system('cls' if os.name == 'nt' else 'clear')
    print('=' * 5,'JOGO INICIADO!','=' * 5)
    


    escolha_usuario = input('Qual a sua jogada?\nPedra\nPapel\nTesoura\n').lower().strip()
    os.system('cls' if os.name == 'nt' else 'clear')

    if escolha_usuario not in ['pedra', 'papel', 'tesoura']:
        print('Essa jogada não vale! Escolha apenas Pedra, Papel ou Tesoura!')
    else:
        print('\nJO...')
        time.sleep(1)
        print('KEN...')
        time.sleep(1)
        print('PÔ!!!')
        time.sleep(0.5)

        os.system('cls' if os.name == 'nt' else 'clear')

        print(f'Eu escolhi {lista}')
        print(f'Você escolheu {escolha_usuario}')

        if escolha_usuario == lista:
            print(f'Hm, empatamos. Vamos tentar de novo?.')
        elif (escolha_usuario == 'pedra' and lista == 'papel') or \
            (escolha_usuario == 'tesoura' and lista == 'pedra') or \
            (escolha_usuario == 'papel' and lista == 'tesoura'): 
            print(f'GANHEI! {lista} vence {escolha_usuario}.')
        else:
            print(f'PARABÉNS! Você ganhou {escolha_usuario} vence {lista}.')

else:
    print('Me avise quando estiver pronto!')