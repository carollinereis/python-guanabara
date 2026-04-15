"""
Refaça o DESAFIO 009, mostrando a tabuada
de um numero que o usuario escolher, so que 
utilizando um laço for.
"""

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(0, 11):
    tab = num * i
    print(f' {num} x {i:2} = {tab:2}')