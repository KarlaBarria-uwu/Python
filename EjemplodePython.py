#Este e s un programa de ejemplo en Python.
#Para ejecutar una parte de este programa, deberás comentar las secciones que no probarás.

#Variables y tipos de datos.
#Aquí se han creado varibles que almacenan un número entero,
#un número decimal, una cadena de texto y un valor booleano.
variable_entera = 42 #Entero
variable_decimal = 3.14 #Decimal
variable_texto = "Hola, mundo!" #Cadena de texto
varible_booleana = True #Valor booleano

#Operadores
#En este caso, resultado_suma almacena el resultado de
#sumar variable_entera y variable_decimal, y comparacion
#almacena el resultado de comparar si variable_entera es
#mayor que variable_decimal.
resultado_suma = varible_entera + variable_decimalcomparacion = (variable_entera > variable_decimal)

#Entrada y Salida
nombre_usuario = input("Por favor, ingresa tu nombre:")
print("Hola,"+nombre_usuario+"¡Este es tu primer programa en Python!.")

#Estructuras de controol de decisiones
#Se utiliza una estructura if-elif-else para tomar decisiones basadas en condiciones
if varible_booleana :
    print("La variable booleana es verdadera.")
elif resultado_suma < 10:
    print("La suma e smenor que 10")
else:
    print("Ninguna de las condiciones anteriores se cumple")
    
    #Colecciones de datos
    #Se crean listas, tuplas, diccionarios y conjuntos para almacenar datos
    lista_numeros = [1,2,3,4,5]
    tupla_colores =("rojo", "verde", "azul")
    dicionario_edades = {"Juan":25, "Maria":30, "Carlos":22}
    conjunto_elementos = {1,2,3,4,5}
    
    #Funciones
    #Se defines una función saludar() y se la utiliza para crear un
    #mensaje de saludo personalizado
    def saludar(nombre):
        return "Hola," +nombre+"!"
    
    mensaje_saludo = saludar ("Estudiante")
    
    #Manejo de errores
    try:
        resultados_division = 0/0
    except ZeroDivisionError:
        print("¡Error! No se puede dividir por cero.")
    finally:
        print("Bloque 'finaly': Este código se ejecuta siempre, haya o no haya errores.")
        
        #Trabajo con archivos
        with open("archivo.txt", "w") as archivo:
            archivo.write("¡Hola desde un archivo!")
            
            #Módulos y bibliotecas
            import math
            mathraiz_cuadrada = math.sqrt(16)
            
            #Porgramación orientada a objetos
            class MiClase:
                def __init__(self, atributo):
                    self.atributo = atributo
                    
                    def mostrar_atributo (self):
                        print ("El valor del atributo es:", self.atributo)
#Manejo d ecadenas (Strings)
longitud_cadena = len("Python")
mayusculas = "hola".upper()
minusculas = "HOLA".lower()
reemplazo = "python es divertido".replace("divertido", "increíble")