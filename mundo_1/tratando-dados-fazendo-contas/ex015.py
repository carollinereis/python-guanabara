"""
Escreva um programa que pergunte a quantidade de Km percorridos por carro alugado e a quantidade 
de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia
e R$0.15 por Km rodado.
"""
# Minha soluçao 
d = float(input('Informe quantos dias o carro foi alugado: '))
r = float(input('Informe quantos kilometros foram rodados: '))

vDia = d * 60
vKm = r * 0.15

vTotal = vDia + vKm

print(f'O total a pagar é de R${vTotal:.2f}')

# Soluçao do professor (mais limpa)

dias = float(input('Quantos dias alugado: '))
km = float(input('Quantos km rodados: '))
pago = (dias * 60) + (km * 0.15)

print(f'O total a pagar é de R${pago:.2f}')
