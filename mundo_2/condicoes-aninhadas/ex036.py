"""
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa,
o salario do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder
30% do salario ou então o emprestimo sera negado.
"""


vcasa = float(input('Qual o valor do imóvel? ').replace('.', '').replace(',', '.'))
slrio = float(input('Qual o seu salário? ').replace('.', '').replace(',', '.'))
anos = int(input('Em quantos anos você deseja pagar? '))

meses = anos * 12
prestacao = vcasa / meses
limite = slrio * 0.30

if prestacao <= limite:
    print(f'PARABÉNS, seu emprestimo foi aprovado! Suas parcelas serão de R${prestacao:.2f} nos próximos {anos} anos.')
else:
    print(f'Emprestimo negado. A prestação de {prestacao:.2f} excede os 30% do seu salário R${slrio}.')

    