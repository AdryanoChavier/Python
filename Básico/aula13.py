nome = 'Adryano Chavier'
altura = 1.80
peso = 95
imc = peso / altura ** 2

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura'
linha_2 = f'Pesa {peso} quilos e seu imc é: {imc:.2f}'
print(linha_1)
print(linha_2)