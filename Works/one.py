# Задание 2_2. Найти сумму чисел списка стоящих на нечетной позиции

import random

def list_generation():
    n = int(input('Количество элементов списка: '))
    b1 = int(input('Граница 1 диапазона значений элементов списка: '))
    b2 = int(input('Граница 2 диапазона значений элементов списка: '))
    return [random.randint(min(b1, b2), max(b1, b2)) for i in range(n)]

numbers_list = list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')