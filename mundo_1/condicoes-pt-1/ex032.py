"""
Faça um programa que leia um ano qualquer e 
mostre se ele é bissexto
"""

ano = int(input('Digite o ano que você nasceu: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        
        if ano % 400 == 0:
            print('Você nasceu em um ano BISSEXTO!')
        else:
            print('Você NÃO nasceu em um ano bissexto!')
    else:
        
        print('Você nasceu em um ano BISSEXTO!')
else:
    
    print('Você NÃO nasceu em um ano bissexto!')