#Entradas
babyWeight=float(input("Ingrese el peso del bebé en libras: "))
babyAge=int(input("Ingrese la edad del bebé en meses: "))

#Proceso
doseVaccination= (babyWeight+10 / babyAge*10)*8

#Salida

print("La dosis de vacuna a aplicar al bebé es de ", round(doseVaccination,2))

