# Калькулятор с комплексными и рациональными числами

import calc_complex
import calc_racio
import datetime
import logging

while True:
    now=datetime.datetime.now()
    logging.log('START')
    logging.log(str(now))
    print('Добро пожаловать в калькулятор')
    print('Какие числа будем складывать? Введите цифру меню: ')
    print('1-Комплексные')
    print('2-Рациональные')
    print('3-выход из меню')
    try:
        type_num=int(input())
        if type_num==1:
            calc_complex.calc_comp_num()
        if type_num==2:
            calc_racio.calc_rac_num()
        elif type_num==3:
            print('Спасибо за использование калькулятора. Возвращайтесь!')
            now=datetime.datetime.now()
            logging.log(str(now))
            logging.log('END')
            break
        else:
            print('Введите число 1 или 2')
    except:
        print('Введите число 1 или 2')