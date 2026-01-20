"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço,
com 5% de desconto.
"""

preco = float(input('Insira o valor do produto: R$ '))

desconto = preco * 0.05
preco_desconto = preco - desconto

print(f'O valor com 5% de desconto é de R${preco_desconto:.2f}')