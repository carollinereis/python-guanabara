"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos digitos separados.
"""

n = int(input('Digite um número de 0 a 9999: '))
num = str(n)

print(f'unidade: {num[3]}')
print(f'dezena: {num[2]}')
print(f'centena: {num[1]}')
print(f'milhar: {num[0]}')



