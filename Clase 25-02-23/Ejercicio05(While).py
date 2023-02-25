#Bucle While
contin="S" #Declaracion de variable que hace verdadera la condición del while
count=0
total=0

while contin=="S" or contin=="s":
    price=int(input('Ingrese el precio del producto\n'))
    quantity=int(input('Ingrese la cantidad del producto producto\n'))
    contin=input('Desea continuar (S) o (N)\n')
    count+=1
    res=price*quantity
    total=total+res

