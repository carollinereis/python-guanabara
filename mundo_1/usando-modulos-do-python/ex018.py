"""
Faça um programa que leia um angulo qualquer e mostre
na tela o valor de seno, cosseno, e tangente desse angulo.
"""
import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}, COSSENO de {cos:.2f}, e TANGENTE de {tan:.2f}')