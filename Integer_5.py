import math
A = input('Введите А: ')
B = input('Введите B: ')
A = int(A)
B = int(B)

#num = math.floor(A/B)
num = A%B
print(num)
