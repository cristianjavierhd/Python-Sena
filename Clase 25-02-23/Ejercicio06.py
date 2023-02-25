#Entradas
budget=int(input('Ingrese cual es el valor de su presupuesto:\n'))
print("¿Desea registrar un gasto? (S) o (N):")
conf=input()
cont=0
totalExpense=0

#Bucle
while conf=="S":
    cont+=1
    if cont==4:
        print("--------------------------","\nRecuerde que solo puede registrar tres gastos por dia")
        break
    expense=int(input("Registre el valor de su gasto\n"))
    budget-=expense
    totalExpense+=expense
    print("--------------------------","\nSu gasto fue de $",expense,"el valor restante de su presupuesto es $",budget,"\n--------------------------")
    print("¿Desea registrar un gasto? (S) o (N)")
    conf=input()    
print("--------------------------","\nSus presupuesto final es de $", budget,"\nRecuerde que el total de sus gastos de hoy fueron de $",totalExpense)

