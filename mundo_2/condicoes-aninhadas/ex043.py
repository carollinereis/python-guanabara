"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule
seu IMC e mostre seu status, de acordo com a tabela abaixo:
Abaixo de 18,5: Abaixo do peso.
18,5 a 24,9: Peso normal.
25,0 a 29,9: Sobrepeso.
30,0 a 34,9: Obesidade grau 1.
35,0 a 39,9: Obesidade grau 2.
40 ou mais: Obesidade mórbida
"""

peso = float(input('Digite seu peso (kg): '))
altura = float(input('Digite sua altura (m): '))

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está com o peso normal.')
elif imc > 25 and imc <= 29.9:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está com sobrepeso.')
elif imc > 30 and imc <= 34.9:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está com obesidade grau I.')
elif imc > 35 and imc <= 39.9:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está com obesidade grau II.')
else:
    print(f'O IMC dessa pessoa é de {imc:.1f}\nEla está com obesidade mórbida!')