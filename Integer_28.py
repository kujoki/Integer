m = int(input('Enter day: '))
n = int(input('Enter first day: '))

k = (m + n - 1)%7

if k == 4:
    print('четверг')
elif k == 5:
    print('пятница')
elif k == 6:
    print('суббота')
elif k == 0:
    print('воскресенье')
elif k == 1:
    print('понедельник')
elif k == 2:
    print('вторник')
elif k == 3:
    print ('среда')
else:
    print ('Ошибка в рассуждениях')
