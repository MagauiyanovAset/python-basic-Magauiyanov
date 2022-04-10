"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def func_pr(pr_numbers):
    result_pr = []
    for pr_number in pr_numbers:
        for num in range(2, pr_number):
            if pr_number % num == 0:
                break
        else:
            if pr_number > 1:
                result_pr.append(pr_number)
    return result_pr



def filter_numbers(numbers_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

     filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
     filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

    if filter_type is ODD:
        return [number for number in numbers_list if number % 2 != 0]

    if filter_type is EVEN:
        return [number for number in numbers_list if number % 2 == 0]

    if filter_type is PRIME:
        return func_pr(numbers_list)
