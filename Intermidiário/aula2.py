"""
Argumentos nomeados e não nomeados em funções python
Argumentos nomeados tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #Definição
    print(f'{x=} y={y} {z=}','|','x + y + z = ', x + y + z)

soma(1 , 2 , 3 )
soma(1,y=2,z=5)