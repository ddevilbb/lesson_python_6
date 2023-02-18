# Практическое задание 1

print('Заполните массив элементами арифметической прогрессии. '
      'Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. '
      'Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.')


def input_variable(name, is_natural=False):
    while True:
        try:
            input_var = int(input(f'Введите {name}:'))
            if is_natural and input_var < 1:
                raise ValueError
            return input_var
        except ValueError:
            print(f'Допустимые значения: любое {"натуральное" if is_natural else "целое"} число')


a1 = input_variable('a1')
d = input_variable('d')
n = input_variable('n', True)

result = []

for i in range(n):
    number = a1 + i * d
    result.append(number)

print(result)
