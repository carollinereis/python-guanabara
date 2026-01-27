"""
Faça um programa que leia uma frase pelo teclado 
e mostre:
- Quantas vezes aparece a letra 'A'
- Em que posicao ela aparece a primeira vez
- Em que posicao ela aparece na ultima vez
"""

frase = str(input('Digite uma frase: ')).strip()
frase1 = frase.count('A')
frase2 = (frase.find('A')+1) # insere +1 para iniciar contagem a partir de 1 ao inves de 0
frase3 = (frase.rfind('A')+1) 

print(f'A letra A aparece {frase1} vezes.')
print(f'A letra A aparece pela primeira vez na posição {frase2}')
print(f'A letra A aparece pela última vez na posição {frase3}')