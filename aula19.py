entrada = input ('[E]ntrar [S]air: ')
senha = input('Senha: ')

senha_permitida = '12345'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrar')
else:
    print('Sair')