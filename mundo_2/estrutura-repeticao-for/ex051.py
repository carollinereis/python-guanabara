"""
Desenvolva um programa que leia o primeiro termo e a razao de uma Progressao Aritmetica.
No final, mostre os 10 primeiros termos dessa progressao
"""

t = int(input('Digite o termo: '))
r = int(input('Digite a razão: '))

for i in range(0, 10):
    termo_atual = t + (i * r)
    print(f'{termo_atual}')
