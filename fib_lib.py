import numpy


class FibNum:
    def __init__(self):
        pass

    def make_value(self, value):
        pass

    def fib_val(self):
        pass

    def dec_val(self):
        pass

    def factorize(self):
        '''разожение числа на множители в системе Фибоначчи'''
        pass

    def __int__(self):
        pass

    def __float__(self):
        pass

    def __add__(self, other):
        pass

    def __radd__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __rsub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __rmul__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __rtruediv__(self, other):
        pass
    # можно дописаль методы целочисленного деления, оствтка отделения, divmod и возведения в чтепень


class FibInt(FibNum):
    def __init__(self, value):
        self._fib_val = self.make_value(value)

    def make_value(self, value) -> str:
        '''для корректного переведения числа в систему счисления Фибоначчи
        числа фибоначчи используются начина со второй единицы последовательности:
        0, 1, |1, 2, 3...'''
        if value == 0:
            return '0'

        # пока работает криво и только для натуральных чисел
        # реализовать с помощью numpy

        # случай, где value = 0, уже рассмотрен, а значит можно сразу написать как минимум одну единицу
        fib_val = ''
        prev_fib_num, curr_fib_num = 1, 1
        # В СТРООООООООООООООООООООООКУУУ!!!
        while curr_fib_num <= value:
            prev_fib_num, curr_fib_num = curr_fib_num, prev_fib_num + curr_fib_num
        # эта строка лишняя: её можно запихнуть в вышестоящий цикл (кажется)
        prev_fib_num, curr_fib_num = curr_fib_num - prev_fib_num, prev_fib_num

        while value != 0:
            if curr_fib_num <= value:
                value -= curr_fib_num
                # можно после 1 сразку добавлять 0, так как разложени не даст дыух единиц подряд
                fib_val += '1'
            else:
                fib_val += '0'
            prev_fib_num, curr_fib_num, = curr_fib_num - prev_fib_num, prev_fib_num

        return fib_val

    def fib_val(self):
        return self._fib_val

    def dec_val(self):
        # сделать получение с помощью numpy
        pass


class FibFloat(FibNum):
    def __init__(self, value):
        self._fib_val = self.make_value(value)

    def make_value(self, value):
        pass

    def fib_val(self):
        return self._fib_val

    def dec_val(self):
        # сделать получение с помощью numpy
        pass
