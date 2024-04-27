
print("Ingresar los datos de la venta")
cliente = input("Ingrese el nombre del cliente: ")
precio1 = int(input("Ingrese el precio del producto1: "))

#Linea incognita 1, solo habia que copiar las lineas de codigos de las otras variables de cantidad
cantidad1 = int(input("Ingrese la cantidad del producto1: "))

precio2 = int(input("Ingrese el precio del producto2: "))
cantidad2 = int(input("Ingrese la cantidad del producto2: "))
precio3 = int(input("Ingrese el precio del producto3: "))
cantidad3 = int(input("Ingrese la cantidad del producto3: "))
descuento = int(input("Ingrese el decuento: "))

total_bruto = (precio1 * cantidad1) +  (precio2 * cantidad2) +  (precio2 * cantidad2)
precio_con_descuento = round(total_bruto - (total_bruto * descuento/100))

#Linea incognita 2, estas 2 lineas de codigo para resolver, las que si resolvi :v
iva = round(precio_con_descuento*0.19) #para sacar iva es con 0.19 por que si lo haces por 1.19 lo sumaras al valor base
total = precio_con_descuento + iva

print("")
print(f"Cliente: \t{cliente}")
print(f"Total bruto: \t${total_bruto}") 

#Linea incognita 3, la cual resolvi :v copiar y pegar otra linea y cambiar variable
print(f"Total desc.: \t${precio_con_descuento}") 

print(f"Iva: \t\t${iva}")
print(f"Total: \t\t${precio_con_descuento + iva}")



