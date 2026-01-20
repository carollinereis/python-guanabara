"""
Escreva um programa que leia um valor em metros 
e o exiba convertido em centimetros e milimitros
"""

valor_m = float(input('Insira o valor em metros: '))
valor_c = valor_m * 100
valor_mi = valor_m * 1000

print(f'A media de {valor_m}m, corresponde a {valor_c:.0f}cm, e {valor_mi:.0f}mm.')