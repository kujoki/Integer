while True:
    m = int(input('Enter num: '))
    import math
    k = m%7

    if k == 1:
        print('понедельник')
    elif k == 2:
        print('вторник')
    elif k == 3:
        print('среда')
    elif k == 4:
        print('четверг')
    elif k == 5:
        print('пятница')
    elif k == 6:
        print('суббота')
    elif k == 0:
        print ('воскресенье')
    else:
        print ('Ошибка в рассуждениях')
