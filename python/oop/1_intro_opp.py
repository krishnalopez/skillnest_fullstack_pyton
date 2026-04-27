#Creación de la clase usuario-entidad
class Usuario:
    def __init__(self): #Constructor
        self.nombre = "Nariyoshi"
        self.apellido = "Miyagi"
        self.email = "miyagi@codingdojo.la"
        self.limite_credito = 30000
        self.saldo_pagar = 0

#Instancias de una clase
miyagi = Usuario()
daniel = Usuario()
krishna = Usuario()

#Valores nueva instancia
krishna.nombre = " Krishna"
krishna.apellido = " Hernandez"
krishna.email = " krishna@gmail.com"
krishna.limite_credito = 1000
krishna.saldo_pagar = 20000
#Accedemos a los atributos de la instancia
print(miyagi.nombre) #Imprime: Nariyoshi
print(miyagi.apellido) #Imprime: Nariyoshi
print(miyagi.email) #Imprime: Nariyoshi
print(miyagi.limite_credito) #Imprime: Nariyoshi
print(miyagi.saldo_pagar) #Imprime: Nariyoshi

#Nuevos valores asignados
daniel.nombre = " Daniel"
daniel.apellido = " Larusso"
daniel.email = " daniel@codingdojo.la"
daniel.limite_credito = 100000
daniel.saldo_pagar = 30000
#Imprimir nombre de cada instancia
print(miyagi.nombre)
print(daniel.nombre)
print(krishna.nombre)