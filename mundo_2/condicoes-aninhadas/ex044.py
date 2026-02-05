"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando
seu preço normal e condição de pagamento.
a vista: dinheiro/cheque: 10% desconto
a vista no cartao: 5% de desconto
em 2x no cartao preço normal
3x ou mais no cartao 20% juros
"""
import os

valor_prod = float(input('Insira o valor do produto: '))
opcao_pag = int(input('Selecione a forma de pagamento:\n[1] à vista no dinheiro/cheque\n[2] à vista no cartão\n[3] 2x no cartão\n[4] 3x ou mais no cartão\n'))

if opcao_pag == 1:
    print(f'Pagando à vista no dinheiro/cheque você tem 10% de desconto. O valor final do produto será de R${valor_prod - (valor_prod * 0.10):.2f}')
elif opcao_pag == 2:
    print(f'Pagando à vista no cartão você tem 5% de desconto. O valor final do produto sairá por R${valor_prod - (valor_prod * 0.05):.2f}')
elif opcao_pag == 3:
    print(f'Seu produto parcelado em 2x no cartão sairá por R${valor_prod:.2f}')
elif opcao_pag == 4:
    parcelas = int(input('Em quantas parcelas? '))
    val_par = valor_prod + (valor_prod * 0.20)
    print(f'Seu produto parcelado em {parcelas} no cartão terá 20% de juros e o total será R${val_par:.2f} com parcelas de R${(val_par / parcelas):.2f}')
else:
    print('Por favor, selecione apenas as opções apresentadas.')