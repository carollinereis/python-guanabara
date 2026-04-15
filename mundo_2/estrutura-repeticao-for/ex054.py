"""
Crie um programa que leia o nascimento de sete pessoas. No final,
mostre quantas pessoas ainda nao atingiram a maioridade e quantos já
são maiores.
"""
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0

for p in range(1, 8):
    ano_nasc = int(input('Digite seu ano de nascimento: '))
    idade = atual - ano_nasc

    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade.')
print(f'Ao todo tivemos {totmenor} menores de idade.')