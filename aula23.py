"""
    Formatação básica de strings
    s - string
    d - int
    f - float
    .<número de dígitos>f
    x ou X - Hexadecimal
    (Caractere)(><^)(quantidade)
    > - Esqueirda
    < - Direita
    ^ - Centro
    Sinal - + ou -
    Ex.: 0 >- 100,.1f
    Conversion flags - !r !s !a
"""
variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel:-<10}.')
print(f'{variavel:0^10}.')