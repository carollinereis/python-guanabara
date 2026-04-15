## repetiçoes controladas

# for c in range(1,10):
#     passo
# pega

# for c in range (0,3):
#     if moeda:
#         pega
#     passo
#     pula
# passo
# pega

for c in range(1,6):  #printa numeros de forma crescente
    print(c)
print('FIM')

for c in range(0,6):  # printa a palavra 'oi' 6x
    print('oi')
print('FIM')

for c in range(7, 0, -1):  #printa de forma decrescente
    print(c)
print('FIM')

for c in range(0, 7, 2):   #printa de 0 a 7 pulando 2 casa. 
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n):               # CONTA até um numero anterior ao digitado pelo usuario
    print(c)
print('FIM')

n = int(input('Digite um numero: '))
for c in range(0, n+1):               # CONTA até um numero exato digitado pelo usuario
    print(c)
print('FIM')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')

for c in range(0, 3): # printa o comando abaixo 3x ou qtas vezes foi colocado dentro de range()
    n = int(input('Digite um valor: ')) 
print('fim')

s = 0 
for c in range(0, 2):
    n = int(input('Digite um valor: ')) 
    s += n # ou (s = s + n) # soma os numeros digitados acima
print(f'A soma de todos os valores é de {s}.')
