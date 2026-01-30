"""
Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para inferiores ou iguais o aumento é de 15%.
"""

sal = float(input('Digite seu salário: '))

if sal >= 1250:
    print(f'Parabéns, seu novo salário com aumento é de R${(sal * 0.10) + sal:.2f}')
else:
    print(f'Parabéns, seu novo salario com aumento é de é de R${(sal * 0.15) + sal:.2f}')