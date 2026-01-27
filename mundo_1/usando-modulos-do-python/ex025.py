"""
Crie um programa que leia o nome de uma pessoa 
e diga se ela tem "SILVA" no nome. 
"""

nome = str(input('Qual seu nome completo? ')).strip()
print(f'Seu nome tem Silva? {"Silva" in nome}')
