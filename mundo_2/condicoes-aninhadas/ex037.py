"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usúario escolher qual será a base de conversão:
- 1 para binário
- 2 para octal 
- 3 hexadecimal
"""

num = int(input('Digite um número inteiro: '))
base = int(input('Qual será a base de conversão? Digite:\n [1] para binário:\n [2] para octal:\n [3] para hexadecimal:\n '))

if base == 1:
    print(f'{num} convertido em binário é de {bin(num)[2:]}')
elif base == 2:
    print(f'{num} convertido em octal é de {oct(num)[2:]}')
elif base == 3:
    print(f'{num} convertido em hexadecimal é de {hex(num)[2:]}')
else:
    print('Por favor digite apenas as opções listadas.')