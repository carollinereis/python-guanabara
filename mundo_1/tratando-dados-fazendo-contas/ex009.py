"""
Faça um programa que leia um número inteiro qualquer e mostre sua tabuada
"""
# Minha soluça0
# valor = int(input('Escolha um número de 1 a 10: '))

# for i in range(1, 11):
#     resultado = valor * i
#     print(f'{valor} * {i} = {resultado}')

#Soluçao professor

num = int(input('Escolha um número para ver sua tabuada: '))
print('{} x {:2} = {}'.format(num, 1, num*1))
print('{} x {:2} = {}'.format(num, 3, num*3))
print('{} x {:2} = {}'.format(num, 4, num*4))
print('{} x {:2} = {}'.format(num, 5, num*5))
print('{} x {:2} = {}'.format(num, 6, num*6))
print('{} x {:2} = {}'.format(num, 7, num*7))
print('{} x {:2} = {}'.format(num, 8, num*8))
print('{} x {:2} = {}'.format(num, 9, num*9))
print('{} x {:2} = {}'.format(num, 10, num*10))