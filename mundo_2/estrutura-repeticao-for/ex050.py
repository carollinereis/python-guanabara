"""
Desenvolva um programa que leia seis numeros inteiros e mostre a soma
apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o
"""

s = 0

for i in range(1, 7):
    n = int(input(f'Digite o {i}º valor inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos valores pares é de {s}')