"""
Escreva um programa que faça o computador 'pensar' em um 
numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir
qual foi o numero escolhido pelo computador.
"""

import random

numcomp = random.randint(0, 5)
tusuario = int(input('Tente adivinhar um número de 0 a 5: '))

if tusuario == numcomp:
    print('Parabéns! Você venceu!')
else:
    print('Que pena, você perdeu!')
