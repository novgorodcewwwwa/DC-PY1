# TODO написать функцию для получения списка уникальных целых чисел

from random import randint


def Unique_list_numbers() -> list[int]:
    length = 15
    min_ = -10
    max_ = 10
    list_unique_num = []
    while len(list_unique_num) != length:
        rand_val = randint(min_, max_)
        if rand_val not in list_unique_num:
            list_unique_num.append(rand_val)
    return list_unique_num


list_unique_numbers = Unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
