"""
Faça um algoritmo que leia o salario de um funcionário e mostre
seu novo salário, com 15% de aumento.
"""

salario = float(input('Insira seu salário atual: R$ '))

aumento = salario * 0.15
salario_aumento = salario + aumento

print(f'Parabéns! Seu novo salário com o aumento de 15% é de R$ {salario_aumento:,.2f}')