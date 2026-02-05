# CONDIÇÕES ANINHADAS

# carro.siga()
# if carro.esquerda():
#     carro.siga()
#     carro.direita()
#     carro.siga()
#     carro.direita()
#     carro.esquerda()
#     carro.siga()
#     carro.direita()
#     carro.siga()
# elif carro.direita():
#     carro.siga()
#     carro.esquerda()
#     carro.siga()
#     carro.esquerda()
#     carro.siga()
# else:
#     carro.siga()
# carro.pare()

nome = str(input('Qual é seu nome? '))
if nome == 'Carol':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia {nome}')