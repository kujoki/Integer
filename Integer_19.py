a = int(input('Enter sec: '))
min = a//60
print(min, 'min')

a = int(input('Enter sec: '))
hours = a//360
print(hours, 'hours')

a = int(input('Enter sec: '))
min_last = a%60
print(min_last, 'last min')

a = int(input('Enter sec: '))
hours_last = a%360
print(hours_last, 'last hours')

a = int(input('Enter sec: '))
min = (a//360)//60
sec = a - min
print(min, 'min')

