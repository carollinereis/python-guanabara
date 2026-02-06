"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na 
tela uma mensagem:

- o primeiro valor é maior
- o segundo valor é menor
- nao existe valor maior, os dois são iguais
"""

num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))

if num1 > num2:
    print(f'O primeiro valor é maior!')
elif num1 < num2:
    print(f'O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais.')