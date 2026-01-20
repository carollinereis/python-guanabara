"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule sua área e a quantidade de tinta necessária para pintá-la, 
sabendo que cada litro de tinta pinta uma area de 2m quadrados
"""

parede_L = float(input('Insira a largura da parede a ser pintada: '))
parede_A = float(input('Insira a altura da parede a ser pintada: '))
litro_tinta = 2

metroQ = parede_L * parede_A
qde_tinta = metroQ / litro_tinta


print(f'A parede tem {metroQ:.1f} m² e será necessário {qde_tinta:.1f} litros de tinta.')

