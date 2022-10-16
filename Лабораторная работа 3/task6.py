list_numbers = [2, -93, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO Оформить решение
max_index = 0
max_list = list_numbers[max_index]
last_index = 0
last_value = 0

for i, current_ in enumerate(list_numbers):
    max_list = list_numbers[max_index]
    if current_ > max_list:
        max_index = i
        max_list = list_numbers[max_index]

last_value = list_numbers[len(list_numbers) - 1]
last_index = len(list_numbers)

list_numbers[len(list_numbers) - 1], list_numbers[max_index] = max_list, last_value

print(list_numbers)
