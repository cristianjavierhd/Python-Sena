#Entrada
num1=int(input("Ingrese el primer número: \n"))
num2=int(input("Ingrese el segundo número: \n"))

#Proceso
if num1>num2:
    print("El número mayor es",num1)
if num1<num2:
    print("El número mayor es",num2)
if num1==num2:
    print("Los números",num1, "y",num2, "son iguales")
else:
    print("Los datos son incorrectos")
