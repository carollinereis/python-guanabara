"""
Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

valor = int(input('Insira um valor: '))
dobro = valor * 2
triplo = valor * 3
rquad = valor ** (1/2) 

print(f'O valor inserido é {valor}\nSeu dobro é {dobro}\nSeu triplo é {triplo}\nSua raiz quadrada é {rquad:.2f}')