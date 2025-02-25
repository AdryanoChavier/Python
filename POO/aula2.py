#Métodos em instâncias de classes Python

class Carro:
    def __init__(self,nome):
        self.nome = nome

    #Método é um função que está dentro da class
        
    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()