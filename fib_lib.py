import numpy


class FibNum:
    def __init__(self): ...
    def make_fib_val(self, value):
        pass
    def fib_val(self):
        pass
    def dec_val(self):
        pass
    def factorize(self):
        '''разожение числа на множители в системе Фибоначчи'''
        pass
    def correct_fib_val(self, value):
        '''корректирует запись числав системе счисления Фибоначчи:
        исправляет 11 на 100, 2 на 1001

        для коррекстного разложения мы добавляем бесконечное
        колличество разрядов слева от числа (...00001001) и два
        дополнительных разряда справа от числа (...00001001|00),
        которве будут обозначать два "скрытых"     (     ...85321|10)
        числа последовательности Фибоначчи'''

        # 2 - > 10|01 -> 10
        # 20 -> 100|1 -> 101
        pass
    def _set_val(self, value):
        pass
    def _correct_fib_val(self):
        pass
    def __int__(self): ...
    def __float__(self): ...
    def __add__(self, other): ...
    def __radd__(self, other): ...
    def __sub__(self, other): ...
    def __rsub__(self, other): ...
    def __mul__(self, other): ...
    def __rmul__(self, other): ...
    def __truediv__(self, other): ...
    def __rtruediv__(self, other): ...
    # можно дописаль методы целочисленного деления, остатка отделения, divmod и возведения в степень


class FibInt(FibNum):

    def __init__(self, value):
        # если значение невозможно представить, как int, то выбросится ошибка
        self._fib_val = None
        self._set_val(int(value))

    def make_fib_val(self, value) -> str:
        '''для корректного переведения числа в систему счисления Фибоначчи
        числа фибоначчи используются начина со второй единицы последовательности:
        0, 1, |1, 2, 3...'''
        if value == 0:
            return '0'

        # случай, где value = 0, уже рассмотрен, а значит можно сразу написать как минимум одну единицу
        fib_val = ('+' if value > 0 else '-') + '1'
        value = abs(value)
        prev_fib_num, curr_fib_num = 1, 1

        while curr_fib_num + prev_fib_num <= value:
            prev_fib_num, curr_fib_num = curr_fib_num, prev_fib_num + curr_fib_num

        # "отрабатываем" ту самую единицу
        value -= curr_fib_num
        prev_fib_num, curr_fib_num = curr_fib_num - prev_fib_num, prev_fib_num

        while prev_fib_num != 0:
            if curr_fib_num <= value:
                value -= curr_fib_num
                if curr_fib_num - prev_fib_num != 0:
                    fib_val += '10'
                    prev_fib_num, curr_fib_num, = curr_fib_num - prev_fib_num, prev_fib_num
                else:
                    fib_val += '1'
            else:
                fib_val += '0'
            prev_fib_num, curr_fib_num, = curr_fib_num - prev_fib_num, prev_fib_num

        return fib_val
    def _set_val(self, value):
        self._fib_val = self.make_fib_val(value)

    def correct_fib_val(self, value):
        sign, value = value[:1], value[1:] + '00'

        while value.count('2') != 0:
            index = value.rfind('2')
            if index == 0:
                value = f'10{value[1]}{int(value[2]) + 1}{value[3:]}'
            else:
                value = f'{value[:index-1]}{int(value[index-1]) + 1}0{value[index+1]}{int(value[index+2]) + 1}{value[index+3:]}'

        value = f'{value[:-1]}1'  # так надо.... Так как в начале мы добавили 2 лишних разряда,
        # то теперь нам нужно их грамотно убрать: меняем последний разряд на "1"

        while value.count('11') != 0:
            index = value.find('11')
            if index == 0:
                value = f'100{value[2:]}'
            else:
                value = f'{value[:index-1]}{int(value[index-1]) + 1}00{value[index+2:]}'

        return sign + value[:-2]
    def _correct_fib_val(self):
        self._fib_val = self.correct_fib_val(self._fib_val)

    def fib_val(self):
        return self._fib_val

    def dec_val(self):
        '''получение десятичного записи числа производится при
        помощи матричного умножения:
        (F1, F2) x ((0, 1),
                          (1, 1)) =
        = (F2, F3)'''
        value = 0

        # матрицы
        fib_numbers = numpy.array((1, 2))
        matrix = numpy.array(((0, 1), (1, 1)))
        for power, _ in filter(lambda el: el[1] == '1', enumerate(self._fib_val[::-1], 0)):
            dot = numpy.dot(fib_numbers, numpy.linalg.matrix_power(matrix, power))
            # пибавляем полученное значение
            value += dot[0]

        return value if self._fib_val[0] == '+' else -value


class FibFloat(FibNum):
    def __init__(self, value):
        self._fib_val = self.make_fib_val(value)

    def make_fib_val(self, value):
        pass

    def fib_val(self):
        return self._fib_val

    def dec_val(self):
        # сделать получение с помощью numpy
        pass
