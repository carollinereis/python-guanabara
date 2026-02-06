"""
Refaça o desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo
será formado:

- Equilatero: todos os lados iguais
- isosceles: dois lados iguais
- escaleno: todos os lados diferentes
"""

reta1 = float(input('Digite o comprimento da primeira reta: '))
reta2 = float(input('Digite o comprimento da segunda reta: '))
reta3 = float(input('Digite o comprimento da terceira reta: '))

if (reta1 + reta2) > reta3 and (reta1 + reta3) > reta2 and (reta2 + reta3) > reta1:
    if reta1 != reta2 != reta3 != reta1:
        print('Este é um triangulo escaleno, onde todos os lados são diferentes!')
    elif reta1 == reta2 == reta3:
        print('O triangulo é Equilatero, pois todos os lados são iguais!')
    else:
        print('O triangulo é isosceles, pois há dois lados iguais.')
else:
    print('Os comprimentos não formam um triangulo!')