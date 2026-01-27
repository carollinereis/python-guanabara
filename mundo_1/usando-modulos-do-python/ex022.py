"""
Digite um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiusculas
- O nome com todas minusculas
- Quantas letras ao todo sem considerar espacos
- Quantas letras tem o primeiro nome
"""

nome = (input('Digite seu nome inteiro: ')) # poderia incluir .strip() para remover os espaços antes ou depois do nome mas a forma feita abaixo já retira
nome1 = len(''.join(nome.split()))
nome2 = len(nome.split()[0])

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
print(f'Quantidade de letras sem contar espaços: {nome1}')
print(f'O primeiro nome tem {nome2} letras.')

