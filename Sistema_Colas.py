class Colas:
    def __init__ (self):
        self.colaC = []
        self.colaA = []
        self.contadorC = 0
        self.contadorA = 0
    
    def servicioC(self):
        self.contadorC += 1
        cliente = f'C{self.contadorC}'
        self.colaC.append(cliente)
        print(f'Cliente {cliente} agregado a la cola del servicio C.')

    def servicioA(self):
        self.contadorA += 1
        cliente = f'A{self.contadorA}'
        self.colaA.append(cliente)
        print(f'Cliente {cliente} agregado a la cola del servicio A.')

    def mostrar_colas(self):
        print(f'\nCola del servicio C: {self.colaC}')
        print(f'Cola del servicio A: {self.colaA}\n')

colas = Colas()

while True:
    opción = input("COMPAÑÍA DE SEGUROS. Seleccione uno de nuestros siguientes servicios:"
                   "\n 1. Servicio C"
                   "\n 2. Servicio A"
                   "\n 3. Mostrar cola de clientes"
                   "\n 4. Terminar "
                   "\n")
    
    if opción == "1":
        colas.servicioC()
    elif opción == "2":
        colas.servicioA()
    elif opción == "3":
        colas.mostrar_colas()
    elif opción == "4":
        break
    else:
        print("Algo ha salido mal, vuelva a introducir el turno del cliente.")