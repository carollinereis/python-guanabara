"""
Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo, calcule e mostre
o comprimento da hipotenusa.
"""

# Minha solução
import math  

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hipotenusa = math.hypot(co, ca)

print(f'A hipotenusa mede {hipotenusa:.2f}')

# Soluçao professor 1
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(f'A hipotenusa vai medir {hi:.2f}')


# Soluçao professor 2
from math import hypot  

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hipotenusa = hypot(co, ca)
print(f'A hipotenusa mede {hipotenusa:.2f}')