"""
    Introdução ao try/except
    try -> tentar executar o código
    except -> ocorreu algum erro ao tentar executar
"""
numero_string = input('Vou dobrar o número que vc digitar: ')

try:
    print('STR:', numero_string)
    numero_float = float(numero_string)
    print('FLOAT:',numero_float)
    print(f'O dobro de {numero_string} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')