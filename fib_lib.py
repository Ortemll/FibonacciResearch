from _classes import *


class FibInt(FibNum):
    '''класс целых чисел, представленных в системе счисления Фибоначчи'''

    def __init__(self, *value, is_fib_val=False):

        # если значение невозможно представить, как int, то выбросится ошибка
        if is_fib_val is True:
            self._fib_val, self._sign = value
        else:
            self._fib_val, self._sign = self._fib_val_from_dec(int(value[0]))

    @staticmethod
    def _fib_val_from_dec(value):
        '''для корректного переведения числа в систему счисления Фибоначчи
        числа фибоначчи используются начина со второй единицы последовательности:
        0, 1, |1, 2, 3...'''
        sign = '+'
        if value == 0:
            return '0', sign
        elif value < 0:
            value = -value
            sign = '-'

        # случай, где value = 0, уже рассмотрен, а значит можно сразу написать как минимум одну единицу
        fib_val = '1'
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

        return fib_val, sign

    @staticmethod
    def _dec_val_from_fib(value, sign='+'):
        '''получение десятичного записи числа производится при
        помощи матричного умножения:
        (F1, F2) x ((0, 1),
                          (1, 1)) =
        = (F2, F3)'''
        import numpy as np

        if value == '0':
            return 0

        dec_val = 0
        # матрицы
        fib_numbers = np.array((1, 1))
        matrix = np.array(((0, 1), (1, 1)))
        for power, _ in filter(lambda el: el[1] == '1', enumerate(value[::-1])):
            dot = np.dot(fib_numbers, np.linalg.matrix_power(matrix, power))
            dec_val += dot[1]

        return dec_val if sign == '+' else -dec_val

    @staticmethod
    def _correct_fib_val(value):
        '''в value не должно быть двух идущих подряд двоек:
        102200 - wrong, 101200 - correct'''
        value += '00'

        while '2' in value:
            index = value.rfind('2')
            if index == 0:
                value = f'10{value[1]}{int(value[2]) + 1}{value[3:]}'
            else:
                value = f'{value[:index - 1]}{int(value[index - 1]) + 1}0{value[index + 1]}{int(value[index + 2]) + 1}{value[index + 3:]}'

        value = f'{value[:-1]}1'  # так надо.... Так как в начале мы добавили 2 лишних разряда,
        # то теперь нам нужно их грамотно убрать: меняем последний разряд на "1"

        while '11' in value:
            index = value.find('11')
            if index == 0:
                value = f'100{value[2:]}'
            else:
                value = f'{value[:index - 1]}{int(value[index - 1]) + 1}00{value[index + 2:]}'

        return value[:-2]

    def get_fib_val(self):
        return self._sign + self._fib_val

    def get_dec_val(self):
        return self._dec_val_from_fib(self._fib_val, self._sign)

    @classmethod
    def _true_add(cls, value1, value2):
        '''сложение двух целых неотрицательных чисел в системе счисления фибоначчи.'''
        if len(value1) > len(value2):
            value1, value2 = value2, value1  # value1 должно быть меньше, чем value2
        res_value = value2[:len(value2) - len(value1)]
        for i in range(-len(value1), 0):
            res_value += str(int(value1[i]) + int(value2[i]))
        return cls._correct_fib_val(res_value)

    @classmethod
    def _true_sub(cls, value1, value2):
        sign = '+'
        if value2 > value1:
            value1, value2 = value2, value1  # value1 должно быть больше, чем value2
            sign = '-'

        res_val = list(map(int, value1))
        # при вычитании разность не будет содержать чисел, больше двойки,
        # а каждая двойка в нём будет окружена нулями
        for i in range(-1, -len(value2) - 1, -1):
            if value2[i] == '1':
                if res_val[i] == 0:
                    index = -res_val[i - 1::-1].index(1) + i - 1
                    res_val[index] = 0
                    for j in range(index + 1, i + 1, 2):
                        res_val[j] += 1
                    res_val[min(-1, j + 1)] += 1
                res_val[i] = 0

        return cls._correct_fib_val(''.join(map(str, res_val[res_val.index(1):]))), sign

    @classmethod
    def _true_mul(cls, value1, value2):
        res_val = '0'
        for i in range(-len(value1), 0):
            if value1[i] == '1':
                for j in range(-len(value2), 0):
                    if value2[j] == '1':
                        index = -max(i, j) - 1
                        if i != j:
                            res_val = cls._true_add(res_val,
                                                    '1' + '0001' * (index // 2) + '001' * (index % 2) + '0' * (abs(i - j) - index%2))
                        else:
                            res_val = cls._true_add(res_val, '1' + '0001' * (index // 2) + '01' * (index % 2))
        return res_val


class FibFloat(FibNum):
    '''класс рацианальных чисел, представленных в системе счисления Фибоначчи'''

    def __init__(self, *value,
                 is_fib_val=False):  # учесть знаки при вводе числителя и знаменателя дроби, как целых чисел
        '''значение value можно задавать тремя способами:
        1. <вещественное число/число с плавающей точкой>, is_fib_val=False
        2. <значения числителя дроби фибоначчи - целое число>,
            <значения знаменатель дроби фибоначчи - целое число>, is_fib_val=False
        3. <значения числителя дроби фибоначчи - строка>,
            <значения знаменатель дроби фибоначчи - строка>,
            <знак дроби фибоначчи ("+" или "-")>,is_fib_val=True'''

        if is_fib_val is True:
            self._fib_val = value[:2]
            self._sign = value[-1]
        else:
            self._fib_val, self._sign = self._fib_val_from_dec(*value, is_float=(len(value) == 1))

    @staticmethod
    def _fib_val_from_dec(*value, is_float=True):
        pass
        # '''для корректного переведения числа в систему счисления Фибоначчи
        # числа фибоначчи используются начина со второй единицы последовательности:
        # 0, 1, |1, 2, 3...'''
        # sign = '+'
        # if value == 0:
        #     return '0'
        # elif value < 0:
        #     value = -value
        #     sign = '-'
        #
        # # случай, где value = 0, уже рассмотрен, а значит можно сразу написать как минимум одну единицу
        # fib_val = '1'
        # prev_fib_num, curr_fib_num = 1, 1
        # while curr_fib_num + prev_fib_num <= value:
        #     prev_fib_num, curr_fib_num = curr_fib_num, prev_fib_num + curr_fib_num
        #
        # # "отрабатываем" ту самую единицу
        # value -= curr_fib_num
        # prev_fib_num, curr_fib_num = curr_fib_num - prev_fib_num, prev_fib_num
        #
        # while prev_fib_num != 0:
        #     if curr_fib_num <= value:
        #         value -= curr_fib_num
        #         if curr_fib_num - prev_fib_num != 0:
        #             fib_val += '10'
        #             prev_fib_num, curr_fib_num, = curr_fib_num - prev_fib_num, prev_fib_num
        #         else:
        #             fib_val += '1'
        #     else:
        #         fib_val += '0'
        #     prev_fib_num, curr_fib_num, = curr_fib_num - prev_fib_num, prev_fib_num
        #
        # return fib_val, sign

    @staticmethod
    def _dec_val_from_fib(numerator, denominator, sign='+'):
        pass
        # '''получение десятичного записи числа производится при
        # помощи матричного умножения:
        # (F1, F2) x ((0, 1),
        #                   (1, 1)) =
        # = (F2, F3)'''
        # import numpy as np
        #
        # if value == '0':
        #     return 0
        #
        # dec_val = 0
        # # матрицы
        # fib_numbers = np.array((1, 1))
        # matrix = np.array(((0, 1), (1, 1)))
        # for power, _ in filter(lambda el: el[1] == '1', enumerate(value[::-1])):
        #     dot = np.dot(fib_numbers, np.linalg.matrix_power(matrix, power))
        #     dec_val += dot[1]
        #
        # return dec_val if sign == '+' else -dec_val

    @staticmethod
    def _correct_fib_val(value):
        pass

    def get_fib_val(self):
        pass

    def get_dec_val(self):
        pass


num1 = FibInt(-239749218377237398127361279)
num2 = FibInt(223786267289182738)
num2 *= num1
print(num2.get_fib_val() == FibInt(-239749218377237398127361279*223786267289182738).get_fib_val())
