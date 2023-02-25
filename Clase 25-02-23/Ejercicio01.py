#Bucles
"""for i in range(1,6):

    price=int(input('Ingrese el precio del producto\n'))
    quantity=int(input('Ingrese la cantidad del producto producto\n'))
    print('Aquí estoy dentro del for')

print('Aquí estoy fuera del for')"""

#Solicitar al usuario un numero positivo y mostrar la tabla de multiplicar del 0 al 10 para este numero

numOne=int(input('Ingrese el número que requiera para la tabla de multiplicar\n'))
for i in range(0,11):
    multiTable = numOne*i
    print(numOne,'x',i,"=",multiTable)