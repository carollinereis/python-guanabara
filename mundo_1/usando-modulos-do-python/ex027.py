"""
Escreva um programa que leia o nome completo de uma pessoa
mostrando en seguida o primeiro e o ultimo nome separadamente.
ex: Ana Maria de Souza
primeiro = Ana
ultimo = Souza
"""

nome = str(input('Insira seu nome inteiro: ')).strip()
stnome = nome.split()[0]
lsnome = nome.split()[-1]

print(f'Seu primeiro nome é: {stnome}')
print(f'Seu último nome é: {lsnome}')