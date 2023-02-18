#Entrada
print("Usuario por favor piensa en un número \n"
        "Ahora sumale cinco \n"
        "Ahora al resultado multiplicalo por tres \n"
        "Y por último al resultado de la multipliación restale quince \n"
        "--------------------------------------------------------------")
numUser=int(input("Por favor ingresa el resultado que obtuviste \n"))

#Proceso
numAdv=numUser/3

#Salida
print("El número en que pensaste fue", round(numAdv), "\n"
        "¿Estoy en lo correcto?")

guess=input("Escribe Si o No según sea el caso \n")

#Proceso 2
if guess =="Si":
    print("Soy todo un adivino")
else:
    print("Rectifica las cuentas y te darás cuenta que no me equivoco")
