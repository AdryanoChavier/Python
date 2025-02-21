#Operadores in e not in
#Strings são iteráveis
#  0 1 2 3 4 5 6
#  A D R Y A N O
# -7-6-5-4-3-2-1

nome= 'Adryano'
print(nome[2])
print(nome[-4])
print(10 * '-')
print('A' in nome)
print('Z' not in nome)

seunome =  input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {seunome}')
else:
    print(f'{encontrar} não está em {nome}')