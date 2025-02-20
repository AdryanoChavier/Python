"""
    Faça um programa que peça ao usuário para digitar um número interio,
    informe se este número é pau ao ímpar. Caso o usuário não digite um número inteiro,
    informe que não é um número inteiro.
"""
numero = input('Digite um número inteiro: ')

if numero.isdigit():#Verifica se o número é um inteiro 
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('Número digitado é par')
    else:
        print('Número digitado é impar')
else:
    print('Você não digitou um número inteiro')
