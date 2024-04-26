#ValorNetoDeUnProducto

producto = input ("Ingrese el nombre del producto: ")
valorProducto = int(input("Ingrese el valor del producto: ")) 
valorNeto = float(0.81)                         ##Se debe utilizar float por que se estan utilizando decimales##
valorSinIva = float(valorProducto * valorNeto)

print(f"-----Detalle producto----")
print(f"NOMBRE PRODUCTO: {producto}")
print(f"VALOR PRODUCTO: {valorProducto}")
print(f"VALOR PRODUCTO SIN IVA: {valorSinIva}") ##Es el que dio el profe en la guia##
print("VALOR PRODUCTO SIN IVA", round(valorSinIva,2)) ##Agregando funcion round##