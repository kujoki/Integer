a = int(input('Enter: '))
'''
m = a//100 #цифра слева
k = a%100 #две цифры справа
new = k*10 + m
print (new)
'''
m = a%10 #цифра справа
k = a//10 #две цифры слева
new = m*100 + k
print (new)
