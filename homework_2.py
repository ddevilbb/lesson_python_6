# Практическое задание 2

print('Определить индексы элементов массива (списка), '
      'значения которых принадлежат заданному диапазону '
      '(т.е. не меньше заданного минимума и не больше заданного максимума)')


def input_list():
    while True:
        try:
            return list(map(int, input('Введите список чисел через пробел: ').split()))
        except ValueError:
            print('Допустимые значения: любые целые числа через пробел')


def input_number(name):
    while True:
        try:
            return int(input(f'Введите {name} число: '))
        except ValueError:
            print('Допустимые значения: любое целое число')


_list = input_list()
_min = input_number('минимальное')
_max = input_number('максимальное')
for i in range(len(_list)):
    if _min <= _list[i] <= _max:
        print(i, _list[i])

