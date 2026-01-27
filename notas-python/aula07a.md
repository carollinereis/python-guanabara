# ORDEM DE PRECEDENCIA PYTHON

# 1 ( )
# 2 **
# 3 * / // %
# 4 + -

# para elevar 

# 81**(1/2) = 9.0
# 25**(1/2) = 5.0
# 127**(1/3) = 5.0265…

# print(3 * (5 + 4) ** 2)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma é {s},\no produto é {m},\ne a divisão é {d}') #\n quebra a linha
print(f'Divisão inteira {di} e a potencia é {e}')