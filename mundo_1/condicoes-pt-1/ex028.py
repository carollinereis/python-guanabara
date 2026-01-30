"""
Escreva um programa que faça o computador 'pensar' em um 
numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador.
"""

import random
from time import sleep # feature do professor

numcomp = random.randint(0, 5)
tusuario = int(input('Tente adivinhar um número de 0 a 5: ')) # jogador tenta adivinhar
print('PROCESSANDO…') 
sleep(3)
if tusuario == numcomp:
    print('Parabéns! Você venceu!')
else:
    print(f'Que pena, você perdeu! Eu pensei no número {numcomp} e não {tusuario}!')
