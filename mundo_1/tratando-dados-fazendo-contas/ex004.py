# Faça um programa que leia algo pelo teclado
# e mostre na tela o seu tipo primitivo
# e todas as informações possíveis sobre ele

info_usuario = input('Digite algo: ')

print(f'O tipo primitivo é: {type(info_usuario)}')
print(f'É numérico? {info_usuario.isnumeric()}')
print(f'É alfabético? {info_usuario.isalpha()}')
print(f'É alfanumerico? {info_usuario.isalnum()}')
print(f'É minuscula? {info_usuario.islower()}')
print(f'É maiuscula? {info_usuario.isupper()}')
print(f'Contém espaço? {info_usuario.isspace()}')
print(f'Está capitalizada? {info_usuario.istitle()}')
