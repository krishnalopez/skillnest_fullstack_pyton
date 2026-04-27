# ➡️ Pasar argumentos 
# Para poder personalizar nuestras instancia 
# vamos a pasar algunos argumentos al método 
# __init__ y que de esta manera podamos 
# a los atributos los valores correspondientes.

class Usuario:
    def __init__(self, nombre, apellido, email, limite_credito, saldo_pagar):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.limite_credito = limite_credito
        self.saldo_pagar = saldo_pagar
#creación de instancia
miyagi = Usuario("Nariyoshi", "Miyagi", "miyagi@codingdojo.la", 10000, 0)
daniel = Usuario("Daniel", "Larusso", "daniel@codingdojo.la", 50000, 20000)
krishna = Usuario("krishna", "hernandez", "krishna@gmail.com", 25000, 200)
#Imprimimos valores
print(miyagi.nombre) #Imprime: Nariyoshi
print(daniel.nombre) #Imprime: Daniel


#---------------------------------------
#-------------tarea rápida
'''
Crear una clase Estudiante, y asignarle los siguientes atributos:
(rut, nombre, apellido, especialidad, fecha_nac)
- Crear 3 instancias para la clase con distintos estudiantes.
- Imprir el nombre y apellido concatenado + especialidad
'''
class Estudiantes:
    def __init__(self, rut, nombre, apellido, especialidad, fecha_nac):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.especialidad = especialidad
        self.fecha_nac = fecha_nac
        
krishna = Estudiantes("22895508-6", "krishna", "hernandez", "programación", "12-12-2008")
donovan = Estudiantes("22985643-9", "donovan", "saez", "programación", "03-10-2008")
martin = Estudiantes("21354138-1", "martin", "nuñez", "programación", "10-04-2004")
print(f"{krishna.nombre} {krishna.apellido} estudia {krishna.especialidad}") 
print(f"{donovan.nombre} {donovan.apellido} estudia {donovan.especialidad}")
print(f"{martin.nombre} {martin.apellido} estudia {martin.especialidad}")
