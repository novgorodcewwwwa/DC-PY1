def get_count_char(str_):
    result = {}
    fix_str = str_.lower()
    for char in fix_str:
        if char.isalpha() and char in result:
            result[char] += 1
        else:
            if char.isalpha() and char not in result:
                result[char] = 1
    return result


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))


def percent_of_chars(dict_):
    result = {}
    sum_values = sum(dict_.values())
    for keys in dict_.keys():
        new_value = round(dict_.get(keys) / sum_values * 100, 1)
        result[keys] = new_value
    return result


# print(percent_of_chars(get_count_char(main_str)))

"""
1.(Пункт 3 для того, чтобы 2 раза не считать заглавную и строчную буквы,
П4 исключить пробелы.) - сразу привести все в нижний регистр
2. Пройтись по всем буквам в строке (цикл for...in...)
3. Составить словарь, где видим количество каждой буквы в нижнем регистре

dict{
}
4. П5 про вторую функцию не влиет на ответ, не заложен в проверку
"""
