while True:
    m = int(input('Enter num: '))
    import math
    k = m%7

    if k == 1:
        print('четверг')
    elif k == 2:
        print('пятница')
    elif k == 3:
        print('суббота')
    elif k == 4:
        print('воскресенье')
    elif k == 5:
        print('понедельник')
    elif k == 6:
        print('вторник')
    elif k == 0:
        print ('среда')
    else:
        print ('Ошибка в рассуждениях')
