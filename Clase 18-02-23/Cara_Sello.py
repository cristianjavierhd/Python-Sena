import random

play=random.randint(1,2)

choice=input("Escoga entre Cara o Sello \n")

if play == 1:
    play="cara"
elif play == 2:
    play="sello"
if play == choice:
    print("Eres el ganador \n","Salio", play)
else:
    print("Perdiste\n","Salio", play)