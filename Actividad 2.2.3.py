#MATRICULA COLEGIO
print ("Detalle anualidad colegio")
nombrealumno = input("Ingrese nombre del alumno")
rut = int(input("ingrese rut del alumno"))
curso = int(input("ingrese curso"))
matricula = 25000
mensualidad = 30000
valortotal = (mensualidad * 10) + matricula

print (f"NOMBRE DE ALUMNO: {nombrealumno}")
print (f"RUT DE ALUMNO: {rut}")
print (f"CRUSO MATRICULADO: {curso}")
print (f"Valor Matricula: {matricula}")
print (f"Valor Mensualidad: {mensualidad}")
print (f"VALOR TOTAL A PAGAR: {valortotal}")

#VALOR NETO DE UN PRODUCTO
producto = input ("Ingrese el nombre del producto:")
valorproducto = int(input("Ingrese valor del producto:"))
iva = 19
valorsiniva = (valorproducto / iva)

print(f"Detalle del producto")
print (f"NOMBRE DEL PRODUCTO: {producto}")
print (f"VALOR DE PRODUCTO: {valorproducto}")
print (f"VALOR SIN IVA: {valorsiniva}")



