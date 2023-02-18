#Entradas
milk=input("¿Trajo la leche? \n Digite S o N \n")
bread=input("¿Trajo el pan? \n Digite S o N \n")
eggs=input("¿Trajo los huevos? \n Digite S o N \n")

#Mamá estricta
if milk =="S" and bread=="S" and eggs=="S":
    print("Ya le preparo el desayuno")
else:
    print("Ganchazo")

#Mamá comprensiva
if milk =="S" or bread=="S" or eggs=="S":
    print("Bueno papito")
else:
    print("Tocará decirle a su papá")

