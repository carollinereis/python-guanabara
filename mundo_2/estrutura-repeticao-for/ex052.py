"""
Faça um programa que leia um numero inteiro e diga se ele é ou nao um 
numero primo.
"""

num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
    # Imprime os números que estão sendo testados lado a lado
    print(f'{c}', end=' ')

print(f'\nO número {num} foi divisível {tot} vezes')

if tot == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')