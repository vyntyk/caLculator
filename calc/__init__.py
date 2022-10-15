import div
import mult
import sub
import sum
import complex

def button_click():
    print('1. Рациональные')
    print('2. Комплексные')
    print('3. Выход')
    print('С какими числами будем работать?')
    type_of_number = int(input())

    if type_of_number == 1:
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Деление')
        print('4. Целочисленное деление')
        print('5. Остаток от деление')
        print('6. Умножение')
        print('7. Возведение в степень')
        print('8. Извлечение корня')
        print('Какую операцию будем производить?')
        operation = int(input())

        if operation == 1:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = sum.sum(a, b)
            print('Сумма равна: ', result)
        elif operation == 2:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = sub.sub(a, b)
            print('Разность равна: ', result)
        elif operation == 3:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = div.div(a, b)
            print('Частное равно: ', result)
        elif operation == 4:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = div.int_div(a, b)
            print('Частное от целочисленного деления равно: ', result)
        elif operation == 5:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = div.rem_of_div(a, b)
            print('Остаток от деления равен: ', result)
        elif operation == 6:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = mult.mult(a, b)
            print('Произведение равно: ', result)
        elif operation == 7:
            a = int(input('Введите первое значение: '))
            b = int(input('Введите второе значение: '))
            result = mult.pow(a, b)
            print(f'{a} в степени {b} равно: {result}')
        elif operation == 8:
            a = int(input('Введите значение: '))
            result = mult.mult(a, 0.5)
            print('Квадратный корень равен: ', result)
    
    elif type_of_number == 2:
        print('1. Сложение')
        print('2. Вычитание')
        print('3. Деление')
        print('4. Умножение')
        print('5. Возведение в степень')
        print('6. Извлечение корня')
        print('Какую операцию будем производить?')
        operation = int(input())
        

        if operation == 1:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            b1 = int(input('Введите реальную часть второго числа: '))
            b2 = int(input('Введите мнимую часть второго числа: '))
            b = complex.comp(b1, b2)
            result = sum.sum(a, b)
            print('Сумма равна: ', result)
        elif operation == 2:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            b1 = int(input('Введите реальную часть второго числа: '))
            b2 = int(input('Введите мнимую часть второго числа: '))
            b = complex.comp(b1, b2)
            result = sub.sub(a, b)
            print('Разность равна: ', result)
        elif operation == 3:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            b1 = int(input('Введите реальную часть второго числа: '))
            b2 = int(input('Введите мнимую часть второго числа: '))
            b = complex.comp(b1, b2)
            result = div.div(a, b)
            print('Частное равно: ', result)
        elif operation == 4:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            b1 = int(input('Введите реальную часть второго числа: '))
            b2 = int(input('Введите мнимую часть второго числа: '))
            b = complex.comp(b1, b2)
            result = mult.mult(a, b)
            print('Произведение равно: ', result)
        elif operation == 5:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            b = int(input('Введите значение степени: '))
            result = mult.pow(a, b)
            print(f'{a} в степени {b} равно: {result}')
        elif operation == 6:
            a1 = int(input('Введите реальную часть первого числа: '))
            a2 = int(input('Введите мнимую часть первого числа: '))
            a = complex.comp(a1, a2)
            result = mult.mult(a, 0.5)
            print('Квадратный корень равен: ', result)
    
    elif type_of_number == 3:
        exit()
