import math
A = input('Введите А: ')
A = int(A)

#num = math.floor(A/B)
dozen = A//10
unit = A%10
print('Число десятков',dozen,'Число единиц', unit)
