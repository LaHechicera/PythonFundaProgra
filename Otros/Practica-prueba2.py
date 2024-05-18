print(" ")
print("-----Calculo de costo de envio-----")
print(" ")
print("Costo base de envio es de $5.000 CLP")
print("Costo por Kg adicional es de $500 CLP")
print(" ")
print("*Si distancia es de más de 100 Km se cobra un adicional de $100 CLP*")
print(" ")

costoBase = 5000
kgAdic = 500
kmAdic = 100

while True:
    nomC = input("Ingrese su nombre: ")
    if len(nomC) > 30:
        print ("Introduzca nombre valido con menos de 30 caracteres")
    elif len(nomC) == 0:
        print ("Nombre no debe quedar vacio")
    else:
        break

while True:
    try:
        paque = float(input("Ingrese el peso del paguete en Kg (Ejemplo: 1.3): "))
        break
    except ValueError:
        print ("Ingrese un valor valido")   

while True:
    try:
        kiloMe = float(input("Ingrese la distancia del envio en Km (Ejemplo: 23): "))
        break
    except ValueError:
        print ("Ingrese un valor valido") 

costoKilo = paque*kgAdic
costoTotal = costoBase+costoKilo

if kiloMe <= 100:
    costoTotal
else:
    kiloMe > 100
    costoTotal += ((kiloMe-100)*kmAdic)

if kiloMe > 100:
    exceKm = ((kiloMe-100)*kmAdic)
else:
    exceKm = 0

total = costoTotal

print(" \n ")
print(" **** Desgloce del costo de envío ****")
print(f"Nombre del cliente: {nomC} ")
print(f"Peso del paquete: {paque}Kg")
print(f"Distancia a la que se enviará el paquete: {kiloMe}Km")
print(f"Costo base de envío: ${costoBase} ")
print(f"Costo por Kilo de peso: ${kgAdic}")
print(f"Costo de envío por el exedente de kilometros: {exceKm}")
 
print(f"El costo total del envío es: ${total}")


import datetime
fechaHora = datetime.datetime.now()

with open(f'Envio_{nomC}.txt', 'w') as archivo:
    archivo.write("\n-----Resumen de ventas-----")
    archivo.write("\n ")
    archivo.write(f"\nFecha y hora actual: {fechaHora}")
    archivo.write("\n ")
    archivo.write(f"\nNombre del cliente: {nomC} ")
    archivo.write(f"\nPeso del paquete: {paque}Kg")
    archivo.write(f"\nDistancia a la que se enviara el paquete: {kiloMe}Km")
    archivo.write(f"\nEl costo total del envio es: ${total}")


print ("Se ha creado un archivo con el resumen de envio del paquete")





