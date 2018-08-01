# lesson3

# Задание №5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import sys


def task():
    i = 1
    max_index = 0
    max_value = 0
    negative_number = 0
    array = []

    num = int(input('Сколько элементов массива Вы хотите ввести? (ввдите целое положительно число):  '))

    while i <= num:
        array.append(input('Введите {} число: '.format(i)))
        i += 1

    print('Ваш массив выглядит так: ', array)

    for i in array:

        if int(i) < 0:
            negative_number = int(i)
            for index, value in enumerate(array):
                if int(value) < 0 and int(value) > negative_number:
                    max_index = index
                    max_value = value

    print('Максимально отрицательное число вашего массива = {}, и находится в массиве под индексом {}'.format(max_value,
                                                                                                              max_index))
    return locals()


def calc_mem(func):
    mem_used = 0
    print('*' * 50)

    for index, values in func.items():

        mem_used += sys.getsizeof(values)
        print('Под {} = {} выделено {} памяти'.format(index, values, sys.getsizeof(values)))

    print('*' * 50)
    print('Всего памяти скушали: ', mem_used)


calc_mem(task())
