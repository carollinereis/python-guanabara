#Condições simples e compostas

# tempo = int(input('Quantos anos tem seu carro?: '))

# if tempo <3:
#     print('carro novo')
# else:
#     print('carro velho')
# print('--FIM--')

# # ou

# tempo = int(input('Quantos anos tem seu carro?: '))
# print('carro novo'if tempo<3 else 'carro velho') # condicao simplificada
# print('--FIM--')

# nome = str(input('Qual teu nome? '))
# if nome == 'Carol':
#     print('Que nome bonito você tem!')
# else:
#     print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a primeira nota: '))
m = (n1 + n2)/2
print(f'A sua media foi {m:.1f}')
if m >= 6.0:
    print('Sua media foi boa! PARABENS!')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')

