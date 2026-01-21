import math  

co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))

hipotenusa = math.hypot(co, ca)

print(f'A hipotenusa mede {hipotenusa:.2f}')