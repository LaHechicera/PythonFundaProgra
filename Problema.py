## Problema: Analisis de ventas diarios de la Cafeteria de grano Puerto Montt


print(" ")
print("-----Cantidad de ventas diarias-----")
print(" ")
while True:
    try:
        panCiab = int(input("Ingrese canditad de Pan Ciabatta: "))
        pieLim = int(input("Ingrese cantidad de Pie de Limon: "))
        cafe = int(input("Ingrese cantidad de cafe: "))
        te = int(input("Ingrese cantidad de té :"))
        alfajor = int(input("Ingrese cantidad de alfajor : "))

        panCiabcosto = (panCiab*2000)
        pieLimcosto = (pieLim*3500)
        cafecosto = (cafe*2200)
        tecosto = (te*1600)
        alfajorcosto = (alfajor*1000)

        total = panCiabcosto+pieLimcosto+cafecosto+tecosto+alfajorcosto
        break
    except ValueError:
        print("Favor ingrese un número valido")

print(" ")
print("-----Resumen de ventas-----")
print(" ")
print(f"Total Pan Ciabata: {panCiabcosto}")
print(f"Total Pie de Limón: {pieLimcosto}")
print(f"Total Cafe: {cafecosto}")
print(f"Total té: {tecosto}")
print(f"Total Alfajores: {alfajorcosto}")
print(f"Total ventas: {total}\n")

if total >= 50000:
    print(f"Saco buena venta hoy, un total de {total}")
    print(" ")
else:
    print(f"Sus ventas fueron bajas hoy, un total de {total}")
    print(" ")

