"""
Desenvolva um programa que pergunte a distancia de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0.50 por Km para viagens de até 200Km
e R$0.45 para viagens mais longas.
"""

distancia = float(input('Digite a distância da sua viagem em Km: '))

if distancia <= 200:
    preco = distancia * 0.50
    print(f'O gasto da sua viagem é de R${preco:.2f}')
else:
    preco = distancia * 0.45
    print(f'O preço da sua viagem será de R${preco:.2f}')