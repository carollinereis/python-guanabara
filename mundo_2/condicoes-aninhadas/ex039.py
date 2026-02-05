"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com 
a sua idade:
- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento
"""
from datetime import date

ano_atual = date.today().year

ano_nascimento = int(input('Que ano você nasceu? '))
idade = ano_atual - ano_nascimento
diferenca = 18 - idade

if idade < 18:
    ano = ano_atual + diferenca
    print(f'Você tem tempo! Seu alistamento será em {ano}.')
elif idade == 18:
    print('Você tem {idade} anos. Está na hora de você se alistar ao serviço militar!')
else:
    excedido = idade - 18
    print(f'Você tem {idade} anos. Já se passaram {excedido} anos do seu tempo de alistamento.\nSeu alistamento foi em {ano_atual - excedido}.')