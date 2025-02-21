while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numeros_validos = None
    operador_permitidos = '+-/*'
    n1 = 0
    n2 = 0

    try:
        n1 = float(numero_1)
        n2 = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    
    if operador not in operador_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:')
    
    if operador == '+':
        print(n1 + n2)
    elif operador == '-':
        print(n1 - n2)
    elif operador == '*':
        print(n1 * n2)
    elif operador == '/':
        print(n1 / n2)
    else:
        print('Nunca deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
