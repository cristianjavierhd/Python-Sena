import random
#Entradas
diceOne= random.randint(1,6)
diceTwo=random.randint(1,6)

#Consola
print("El primer dado es:",diceOne,
"\nEl segundo dado es:",diceTwo,
"\n--------------------------------")

#Operaciones
if diceOne == 1 and diceTwo==1 or diceOne==6 and diceTwo==6:
    print("Eres el ganador")

elif diceOne + diceTwo ==3 or diceOne + diceTwo == 11 or diceOne + diceTwo ==7:
    print("Eres el ganador")

else:
    print("Has perdido")