"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajuda ele, lendo o nome deles e escrevendo o nome escolhido.
"""

# Minha soluçao
import random
alunos = random.choice(['Leandro', 'Maria', 'José', 'Eduarda'])

print(f'O aluno escolhido para apagar o quadro é {alunos}')

#Segunda soluçao dando ao usuario a oportunidade de incluir os nomes

import random
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
lista = [al1, al2, al3, al4]

print(f'O aluno escolhido para apagar o quadro é {random.choice(lista)}')