
 # TODO написать функцию генерации случайных паролей

import random
import string


def Random_password(n=8) -> str:
    if not isinstance(n, int):
        raise TypeError
    if not n > 0:
        raise ValueError
    list_digits = string.ascii_uppercase + string.ascii_lowercase + string.digits
    list_password = random.sample(list_digits, n)
    password = "".join(list_password)
    return password


print(Random_password())






