"""
A Confaderasão Nacional de Natação precisa da um programa qua leia o
ano de nascimento de um atleta a mostra sua categoria, de acordo com a idade:

—- Até 9 anos: MIRIM
— Até 14 anos: INFANTIL
—- Até 19 anos: JUNIOR
—- Até 25 anos: SENIOR
—- Acima: MASTER
"""

from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Que ano você nasceu? '))

idade = ano_atual - ano_nascimento

if idade <= 9:
    print('Você está na categoria MIRIM.')
elif idade <= 14:
    print('Você está na categoria INFANTIL.')
elif idade <= 19:
    print('Você está na categoria JUNIOR')
elif idade <= 25:
    print('Você está na categoria SENIOR')
else: 
    print('Você está na categoria MASTER.')
