totalScore=0
for i in range(1,5):
    print('Ingrese la calificación del taller',i)
    score=float(input())
    totalScore+=score
finalScore=totalScore/4
print('----------------------','\nSu nota final es', finalScore,'\n-------------------------------')


if 0.0<=finalScore<=2.9:
    print('Reprobaste la asignatura')
elif 3.0<=finalScore<=4.0:
    print('Pasaste raspando la asignatura')
elif finalScore>4.0:
    print('Aprobaste con buenos resultados')
