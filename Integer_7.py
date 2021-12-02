import math
A = input('Введите А: ')
A = int(A)

#num = math.floor(A/B)
dozen = A//10
unit = A%10
sum = dozen + unit
mult = dozen*unit
print('Сумма',sum,'Произведение', mult)
