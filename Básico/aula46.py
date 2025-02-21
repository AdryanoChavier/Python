"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)#Adiciona
lista.pop() #Remove ultimo valor da lsita
lista.append(60)#Adiciona
lista.append(70)#Adiciona
ultimo_valor = lista.pop(3) #Removendo e adicionando a variavel
print(lista, 'Removido,', ultimo_valor)