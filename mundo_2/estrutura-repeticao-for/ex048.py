"""
Faça um programa que calcule a soma entre todos os numeros impares
que sao multiplos de 3 e que se encontram no intervalo de 1 ate 500
"""

s = 0
for i in range(1, 501, 1):
    if i % 2 != 0 and i % 3 == 0:
        s += i
print(f'A soma entre todos os numeros impares multiplos de 3 é de {s}')

# VERSAO MAIS LIMPA DO PROFESSOR

s = 0
cont = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        cont += 1
        s += i
print(f'A soma de todos os {cont} valores solicitados é de {s}.')

