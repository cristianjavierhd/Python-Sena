#Generar un contador con la referencias ingresadas
count=0 #Definir la variable númerica del contador y definir antes del bucle
total=0
#Bucle
for i in range(0,6):
    price=int(input('Ingrese el precio del producto\n'))
    quantity=int(input('Ingrese la cantidad del producto producto\n'))
    count+=1
    res=price*quantity
    total=total+res
    print('el acumulado de los productos va en',total,'\n---------------------------------')

print('Se registraron',count,'y el subtotal es',total, '\n---------------------------------')

cash=int(input('Ingrese la suma pagada por el cliente\n'))
cashBack=cash-total

print('El cambio que debe darse al cliente es',cashBack,'\n---------------------------------')

movilExt=input('El cliente tiene telefonía móvil éxito (S) o (N)\n')

if movilExt=="S":
    print('---------------------------','\nObtuviste',count,'minutos con tu compra')
else:
    print('---------------------------''\nNo pierdas más minutos, adquiere ya tu telefonía móvil éxito')