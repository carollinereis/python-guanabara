### Manipulando Cadeias de Texto

frase = 'Curso em Video Python'

# Fatiamento

frase[9] # imprime o caracter 9, ou seja letra V
frase[9:13] # imprime imprime letras Vide ou seja de 9 a 12.
frase [9:21:2] #imprime de V ao n MAS pulando de 2 em 2
frase [:5] # quando omitimos de onde deve iniciar, o codigo começa do 0 e vai ate ao indicado
frase[15:] # começa a imprimir de 15 e vai até o final ja que o codigo nao indica onde parar
frase[9:3] # inicia do 9 e pula de 3 em 3

# Analise

len(frase) # qual o comprimento da frase
frase.count('o') # conta quantas letras o tem na frase
frase.count('o', 0, 13) 
frase.find('deo') # encontra 'deo' na frase, indicando onde começou
frase.find('Android') # se nao houver a info na variavel, retorna -1 pois nao foi encontrado
'Curso' in frase # responde TRUE

# Transformaçao

frase.replace('Python', 'Android') # substitui python por android
frase.upper() # deixa tudo maiusculo
frase.lower() # deixa tudo minusculo
frase.capitalize() #deixa a primeira letra maiusculo
frase.title() # deixa todas as palavras com a primeira letra maiuscula

frase1 = '   Aprenda Python  ' # com espaço

frase.strip() # remove espaços desnecessarios antes e depois do string
frase.rstrip() # remove apenas os espaços desnecessarios da direita
frase.lstrip() # remove os espaços desnecessarios da esquerda

# Divisão

frase.split() # gera uma lista para cada palavra da variavel

# juncao

'-'.join(frase) # inclui - entre as letras

# para printar um texto longo faça

print("""Welcome! Are you completely new to programming?
about why and how to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
It's also easy for beginners to use and learn, so jump in!""")

print(frase.replace('Python', 'Android'))
print('Curso' in frase)






