A = int(input('Len(A): '))
B = int(input('Len(B): '))
C = int(input('Len(C): '))

n = A//C
k = B//C

count = n*k

ost_pl = A*B - count*C*C
print ('Число квадратов: ',count, 'Оставшаяся площадь: ', ost_pl)
