


# 1. VARIABLES Y TIPOS DE DATOS

#Crea una variable llamada nombre_empresa y asígnale el valor "TechSolutions".
nombre_empresa = "TechSolutions"

#Crea una variable llamada año_fundacion y asígnale el valor 2010.
año_fundacion = 2010

#Imprime el tipo de dato de ambas variables.
print(nombre_empresa, type(nombre_empresa))
print(año_fundacion, type(año_fundacion))



# 2. ESTRUCTURAS DE CONTROL

#Escribe un programa que pida al usuario ingresar un número y determine si es positivo, negativo o cero.
try:
    numero = int(input("Escribe un número entero: "))
    print("es Positivo" if numero > 0 else "es Negativo" if numero < 0 else "es Cero") # Shorthand If
except ValueError:
    print("ERROR - Se esperaba un número entero")

#Crea un bucle for que imprima los números del 1 al 10.
for i in range(1,11):
    print(i, end = ' ')
print() # salto de línea



# 3. FUNCIONES

#Define una función llamada calcular_iva que tome como parámetro el precio de un producto y devuelva el precio con el IVA (21%) incluido.
def calcular_iva(precioProducto):
    return precioProducto * 1.21

#Llama a la función con un precio de 100 y muestra el resultado.
print(calcular_iva(100))



# 4. LISTAS Y DICCIONARIOS

#Crea una lista llamada empleados con los nombres "Ana", "Carlos", "María" y "Luis".
empleados = ["Ana", "Carlos", "María", "Luis"]

#Añade un nuevo empleado llamado "Pedro" a la lista.
empleados.append("Pedro")

#Crea un diccionario llamado info_empleado con las claves nombre, edad y departamento, y asígnales valores correspondientes.
info_empleado = {"nombre": "Eustaquio", "edad": 77, "departamento": "Finanzas"}

#Imprime el valor asociado a la clave departamento.
print(info_empleado["departamento"])



# 5. PROGRAMACIÓN ORIENTADA A OBJETOS

#Define una clase llamada Producto con los atributos nombre, precio y cantidad.
class Producto(object):
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self): # Equivalente a sobreescribir método toString en otros lenguajes, permite pintar el objeto de forma legible
        return f"{self.nombre} | {self.precio}€ | {self.cantidad}u"

#Crea un método llamado calcular_total que devuelva el precio total del producto (precio * cantidad).
    def calcular_total(self):
        return self.precio * self.cantidad
    
#Crea métodos para aumentar/disminuir la cantidad.
    def aumentar_cantidad(self, aumento):
        self.cantidad += aumento

    def disminuir_cantidad(self, decremento):
        self.cantidad -= decremento

#Crea una instancia de la clase Producto y llama al método calcular_total.
producto_1 = Producto(nombre = "Bolígrafo", precio = 1.45, cantidad = 3)
print(producto_1.calcular_total())

#Crea una instancia de la clase Producto y llama al método aumentar_cantidad.
producto_2 = Producto(nombre = "Lápiz", precio = 0.95, cantidad = 2)
producto_2.aumentar_cantidad(4)

#Crea una instancia de la clase Producto y llama al método disminuir_cantidad.
producto_3 = Producto(nombre = "Libreta", precio = 2.85, cantidad = 5)
producto_3.disminuir_cantidad(4)



# 6. MANEJO DE ARCHIVOS

#Crea un archivo de texto llamado empleados.txt y escribe en él los nombres de los empleados de la lista empleados.
nombreArchivo = "empleados.txt"

try:
    open(nombreArchivo, 'x') # El método open() permite crear, leer y escribir(+adjuntar) archivos
except FileExistsError:
    print(f"El archivo '{nombreArchivo}' ya existe.") # Sin este bloque daría error de ejecución así que los añado por comodidad

with open(nombreArchivo, "w") as archivoTXT:
    for empleado in empleados:
        archivoTXT.write(empleado + ' ') # Escribe valor de la lista y añade espacio en blanco

#Lee el archivo empleados.txt e imprime su contenido.
with open(nombreArchivo, "r") as archivoTXT:
    contenido = archivoTXT.read()
print(contenido)

#Lee un archivo CSV que contenga datos de productos (nombre, precio, cantidad) y crea una lista de objetos Producto a partir de esos datos.
nombreArchivo = "productos.csv"

try:
    open(nombreArchivo, 'x') # Creamos archivo csv
except FileExistsError:
    print(f"El archivo '{nombreArchivo}' ya existe.")

datosArchivo = """nombre,precio,cantidad
Grapadora,2.75,3
Archivador,1.88,2
Pizarra blanca,16.99,1
Separador,4.14,2
Mochila,8.85,1
"""
with open(nombreArchivo, "w") as archivoCSV: # Abrimos y escribimos los datos
    archivoCSV.write(datosArchivo)

listaObjetos = [] # Creamos variable lista objetos

with open(nombreArchivo, "r") as archivoCSV: # Abrimos y leemos los datos
    next(archivoCSV) # Saltamos la primera línea (cabecera)
    for linea in archivoCSV:
        registro = linea.strip("\n").split(",") # strip() elimina salto de línea final, split() separa y crea lista
        listaObjetos.append(Producto(registro[0], registro[1], registro[2]))

for objeto in listaObjetos: # Comprobamos si la lista se ha llenado correctamente
    print(objeto)

