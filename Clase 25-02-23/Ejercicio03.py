countM=0
countF=0
for i in range(0,10):
    sex=input('El sexo de la persona es (H) o (M)\n')
    if sex=='H':
        countM+=1
    else:
        countF+=1
print('La cantidad de hombres en el grupo son:',countM, '\n----------------------------------\n'
    'La cantidad de mujeres en el grupo son:',countF, '\n----------------------------------\n')