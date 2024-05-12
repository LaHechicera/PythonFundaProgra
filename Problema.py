## Problema: Analisis de ventas diarios de la Cafeteria de grano Puerto Montt


print(" ")
print("-----Cantidad de ventas diarias-----")
print(" ")
for i in range(1):
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
    except TypeError:
        print("Favor ingrese un número valido")

    else:
        print(" ")
        print("-----Resumen de ventas-----")
    
    
    finally:
        print(" ")
        print("Total Pan Ciabata: ", panCiabcosto)
        print("Total Pie de Limón: ", pieLimcosto)
        print("Total Cafe: ", cafecosto)
        print("Total té: ", tecosto)
        print("Total Alfajores: ", alfajorcosto)
        print("Total ventas", total)
        print(" ")

if total >= 50000:
    print("Saco buena venta hoy, un total de ", total)
    print(" ")
else:
    print("Sus ventas fueron bajas hoy, un total de ", total)
    print(" ")

