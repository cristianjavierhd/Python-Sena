#Entradas
age=int(input("Ingresa tu edad en años \n"))

#Proceso
if 0<=age<=4:
    print("El cliente ingresa gratis")
elif 4<age<18:
    print("El cliente debe pagar $20.000 para ingresar")
elif 18<=age<=60:
    print("El cliente debe pagar $15.000 para ingresar")
elif age>60:
    print("El cliente debe pagar $3.000 para ingresar")
    