"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere US$1.00 = R$3.27
"""

valor_real = float(input('Quantos reais você tem na carteira? '))

conversao = valor_real / 3.27

print(f'Você consegue comprar {conversao:.2f} dólares com os reais que você tem na carteira.')

