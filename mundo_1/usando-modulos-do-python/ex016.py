"""
Crie um programa que leia um número qualquer pelo teclado e mostre
na tela a sua porçao inteira.
"""

#Minha Soluçao
import math

num = float(input('Digite um número: '))
# num1 = math.trunc(num) 
# print(f'O número {num} tem uma parte inteira {num1}') # como eu fiz primeira vez
print(f'O número {num} tem uma parte inteira {math.trunc(num)}') # forma mais limpa

# Opçao diferente 1

from math import trunc
num = float(input('Digite um número: '))
print(f'O número {num} tem uma parte inteira {trunc(num)}')

# Opcao diferente 2

num = float(input('Digite um número: '))
print(f'O número {num} tem uma parte inteira {int(num)}')

