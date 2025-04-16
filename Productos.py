#VALOR NETO DE UN PRODUCTO
producto = input ("Ingrese el nombre del producto:")
valorproducto = int(input("Ingrese valor del producto:"))
iva = 1.19
valorsiniva = (valorproducto / iva)
valortotal = (valorproducto + iva)

print(f"Detalle del producto")
print (f"NOMBRE DEL PRODUCTO: {producto}")
print (f"VALOR DE PRODUCTO: {valorproducto}")
print (f"VALOR SIN IVA: {valorsiniva}")
print (f"VALOR TOTAL: {valortotal}")
