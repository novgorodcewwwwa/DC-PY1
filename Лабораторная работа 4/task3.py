def delete(list_, index=None):
    if index is None:
        index = -1
    if index >= 0:
        first_part = list_[:index]
        second_part = list_[index+1:]
        return first_part + second_part
    elif index < 0:
        first_part = list_[::-1]
        index = index * (-1) - 1
        second_part = first_part[:index]
        first_part_of_negative = first_part[index+1:]
        second_part_of_negative = second_part + first_part_of_negative
        return second_part_of_negative[::-1]


print(delete([0, 0, 1, 2], index=0))  # [0, 1]
print(delete([0, 1, 1, 2, 3], index=1))  # [0, 1, 2]
print(delete([0, 1, 2, 3, 4, 4]))  # [0, 1, 2, 3]
