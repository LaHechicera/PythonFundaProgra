
print("----Formulario----")
print("A continuación deberas responder unas preguntas referentes a \n\"DC comics\" en su mayoria del universo de Batman por cada \nrespuesta correcta obtendras puntaje (1.0 - 0.5 - 0.2 - 0 respectivamente)")
print(" ")
print("¿Cuál es la identidad secreta de Batgirl original?")
print(" ")
print("A. Barbara Gordon")
print("B. Cassandra Cain")
print("C. Stephaine Brown")
print("D. Harley Quinn")
print(" ")
respt = input("Ingrese su respuesta (Ej: D) ")

if respt == "A":
    print("Respuesta correcta, ganas 1.0 punto")
elif respt == "B":
    print("A pesar de que si fue una Batgirl no es la original, ganas 0.5 puntos")
elif respt == "C":
    print("A pesar de que si fue una Batgirl no es la original, ganas 0.2 puntos")
else:
    print("Harley Quinn es una antiheroe, ganas 0 puntos")

print(" ")
print("¿Cuál es el villano principal de Batman?")
print(" ")
print("A. Salomon Grundy")
print("B. Jim Gordon")
print("C. Joker")
print("D. Gatubela")
print(" ")
respt = input("Ingrese su respuesta ")

if respt == "A":
    print("A pesar de que si es un villano no es el principal, ganas 0.5 punto")
elif respt == "B":
    print("Jim Gordon es el comisionado de policia, ganas 0 puntos")
elif respt == "C":
    print("Respuesta correcta, ganas 1.0 puntos")
else:
    print("Gatubela es una antiheroe, ganas 0.2 puntos")

print(" ")
print("¿Que Robin murio a manos del Joker en el primer comic \"La Muerte en la Familia\"?")
print(" ")
print("A. Dick Grayson")
print("B. Stephanie Brown")
print("C. Victor Szas")
print("D. Jason Todd")
print(" ")
respt = input("Ingrese su respuesta ")

if respt == "A":
    print("Dick Grayson fue el primer Robin pero no murio a manos del Joker, ganas 0.5 punto")
elif respt == "B":
    print("A pesar de que si fue un Robin por más tiempo fue una Batgirl, ganas 0 puntos")
elif respt == "C":
    print("Es un villano, ganas 0.2 puntos")
else:
    print("Respuesta correcta, ganas 1.0 puntos")

