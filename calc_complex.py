import datetime
import logging

def calc_comp_num():
    print('Введите первое комплексное число в формате a+bi. Сначала а1:')
    a1=int(input())
    print('Теперь b1: ')
    b1=int(input())
    print(f'{a1} + {b1} i\n')
    print('Введите второе комплексное число в формате a+bi. Сначала а2:')
    a2=int(input())
    print('Теперь b2: ')
    b2=int(input())
    print(f'{a2} + {b2} i\n')
    print('Введите операцию для вычисления. Можно использовать операции +,-,/,*')
    math_complex=input()

    logging.log(str(f'({a1} + {b1} i) {math_complex} ({a2} + {b2} i)'))


    if math_complex=='+':
        res=a1+a2
        resi=b1+b2
    if math_complex=='-':
        res=a1-a2
        resi=b1-b2
    if math_complex=='*':
        res=a1*a2-b1*b2
        resi=a1*b2+b1*a2
    if math_complex=='/':
        res=round(float((a1*a2+b1*b2)/(a2**2+b2**2)),3)
        resi=round(float((a2*b1-a1*b2)/(a2**2+b2**2)),3)

    print(f'{a1} + {b1} i {math_complex} {a2} + {b2} i = {res} + {resi} i')
    now=datetime.datetime.now()
    logging.log(str(now))
    logging.log(str(f'Результат = {a1} + {b1} i {math_complex} {a2} + {b2} i = {res} + {resi} i'))
    logging.log('END')
