class Colas:
    def __init__(self):
        self.colaA= []
        self.colaB=[]

    def agregar_elementos(self):
        for i in range(5):
            elemento1= int(input("Ingrese un número para la cola A: "))
            elemento2= int(input("Ingrese un número para la cola B: "))
            self.colaA.append(elemento1)
            self.colaB.append(elemento2)
            print(f'Cola A después de agregar "{elemento1}": {self.colaA}')
            print(f'Cola B después de agregar "{elemento2}": {self.colaB}')

    def suma_colas(self):
        cola_resultado= []
        for a, b in zip(self.colaA, self.colaB):
            cola_resultado.append(a + b)
        print(f'Suma de la cola A y cola B: {cola_resultado}')
        return cola_resultado
    
colas = Colas()
colas.agregar_elementos()
resultado = colas.suma_colas()