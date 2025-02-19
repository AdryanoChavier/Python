"""
    Exercício
    Peça ao usuário para digitar seu nome
    Peça ao usuário para didgitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            seu nome é {nome}
            Seu nome invertido é {nome invertido}
            Se nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra so seu nome é {letra}
            a última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpa, você deixou campos vazios."
"""
nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')
    if ' ' in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'Ultima letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios.')