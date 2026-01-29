"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar de 80km/hr mostre uma mensagem que ele foi multado.
A multa vai custar R$7,00 por cada km acima do limite.

"""

vel = int(input('Digite a velocidade do carro: '))
velmax = 80
valorKm = 7
adicional = (vel - velmax) * valorKm
multa = vel + adicional

if vel <= velmax:
    print('Você passou abaixo do limite de velocidade! ')
else:
    print(f'Sua multa é de R${multa}.')