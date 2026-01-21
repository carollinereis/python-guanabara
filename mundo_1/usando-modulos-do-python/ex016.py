"""
Crie um programa que leia um número qualquer pelo teclado e mostre
na tela a sua porçao inteira.
"""
import math

num = float(input('Digite um número: '))
# num1 = math.trunc(num) 
# print(f'O número {num} tem uma parte inteira {num1}') # como eu fiz
print(f'O número {num} tem uma parte inteira {math.trunc(num)}')