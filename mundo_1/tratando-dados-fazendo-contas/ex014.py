"""
Escreva um programa que converta uma temperatura digitada em Celsius para Fahrenheit.
"""
# Minha Soluçao
celsius = float(input('Informe a temperatura em Celsius: '))
conversao = (celsius * 1.8) + 32

print(f'A temperatura é de {conversao}°F')

# Soluçao do professor

c = float(input('Informe a temperatura em °C: '))
f = ((9 * c / 5) + 32)
print('A temperatura de {}°C corresponde a {}°F'.format(c,f))