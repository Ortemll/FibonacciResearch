class FibNum:
    '''базовый класс чисел, представленных в системе счисления Фибоначчи'''
    def __init__(self):
        pass

    @staticmethod
    def fib_val_from_dec(value):
        '''неявно определён для классов FibInt И FibFloat, но имеет своих двойников
        для каждого из них, как метод  _fib_val_from_dec
        разложение числа из десятиричной системы счисления
        в систему счисления фибоначчи
        -в качестве аргумента value передаётся какое-либо десятеричное число
        -возвращает строку нулей и единиц и знак'''
        pass

    @staticmethod
    def dec_val_from_fib(value, sign='+'):
        '''неявно определён для классов FibInt И FibFloat, но имеет своих двойников
        для каждого из них, как метод  _dec_val_from_fib
        -в качестве аргумента value передаётся десятеричное число
        -в качестве аргумента sign может быть переданно два значеня: '+' и '-'.
            они обозначают знак переданного числа
        -возвращает число в десятиричной системе счисления'''
        pass

    @staticmethod
    def correct_fib_val(value):
        '''неявно определён для классов FibInt И FibFloat, но имеет своих двойников
        для каждого из них, как метод  _correct_fib_val
        корректирует запись числав системе счисления Фибоначчи:
        исправляет 11 на 100, 2 на 1001 и т. д.

        для коррекстного разложения мы добавляем бесконечное
        колличество разрядов слева от числа (...00001001) и два
        дополнительных разряда справа от числа (...00001001|00),
        которве будут обозначать два "скрытых"     (     ...85321|10)
        числа последовательности Фибоначчи:
        2 - > 10|01 -> 10
        20 -> 100|1 -> 101

        -в качестве аргумента value передаётся строка, состоящая из любых чисел или список натуральных чисел
        -возвращает строку из нулей и единиц'''
        pass

    def get_fib_val(self):
        '''-возвращает строку нулей и единиц'''
        pass

    def get_dec_val(self):
        '''-возвращает десятиричное число'''
        pass

    @classmethod
    def true_add(cls, value1, value2):
        '''сложение двух неотрицательных чисел в системе счисления фибоначчи.
        неявно определён для классов FibInt И FibFloat, но имеет своих двойников
        для каждого из них, как метод  _true_add
        -value1 и value2 - строки нулей и единиц !не объекты класса FibNum!
        -c помощью cls.correct_fib_val (и cls._correct_fib_val у FibInt и FibFloat) корректирует значение суммы
        -возвращает строку из нулей и единиц'''
        pass

    @classmethod
    def true_sub(cls, value1, value2):
        '''вычетание двух неотрицательных чисел в системе счисления фибоначчи.
        неявно определён для классов FibInt И FibFloat, но имеет своих двойников
        для каждого из них, как метод  _true_sub
        -value1 и value2 - строки нулей и единиц !не объекты класса FibNum!
        -c помощью cls.correct_fib_val (и cls._correct_fib_val у FibInt и FibFloat) корректирует значение разности
        -возвращает строку из нулей и единиц и знак'''
        pass

    @classmethod
    def true_mul(cls, value1, value2):
        '''умножение двух неотрицательных чисел в системе счисления фибоначчи.
          неявно определён для классов FibInt И FibFloat, но имеет своих двойников
          для каждого из них, как метод  _true_mul
          -value1 и value2 - строки нулей и единиц !не объекты класса FibNum!
          -c помощью cls.correct_fib_val (и cls._correct_fib_val у FibInt и FibFloat) корректирует значение произведения
          -возвращает строку из нулей и единиц и знак'''
        pass

    @classmethod
    def true_div(cls, value1, value2): #wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
        pass

    @classmethod
    def true_mod(cls, value1, value2):
        '''щстаток от деления двух неотрицательных чисел в системе счисления фибоначчи.
          неявно определён для классов FibInt И FibFloat, но имеет своих двойников
          для каждого из них, как метод  _true_mod
          -value1 и value2 - строки нулей и единиц !не объекты класса FibNum!
          -c помощью cls.correct_fib_val (и cls._correct_fib_val у FibInt и FibFloat) корректирует значение
          -возвращает строку из нулей и единиц и знак'''
        pass

    # методы сложения, вычитания, умножения и деления должны быть определены здесь
    # учесть, что other может быть объектом любого класса
    def __add__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if (self._sign, other._sign) == ('+', '-'):
                    return self.__class__(*self._true_sub(self._fib_val, other._fib_val), is_fib_val=True)
                elif  (self._sign, other._sign) == ('-', '+'):
                    return self.__class__(*self._true_sub(other._fib_val, self._fib_val), is_fib_val=True)
                return self.__class__(self._true_add(self._fib_val, other._fib_val), self._sign, is_fib_val=True)
            else:
                return None # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            raise TypeError(f'can only add FibNum (not "{other.__class__.__name__}") to FibNum')
    def __iadd__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if (self._sign, other._sign) == ('+', '-'):
                    self._fib_val, self._sign = self._true_sub(self._fib_val, other._fib_val)
                elif (self._sign, other._sign) == ('-', '+'):
                    self._fib_val, self._sign = self._true_sub(other._fib_val, self._fib_val)
                else:
                    self._fib_val = self._true_add(self._fib_val, other._fib_val)
            else:
                self = None  # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return self
        else:
            raise TypeError(f'can only add FibNum (not "{other.__class__.__name__}") to FibNum')

    def __sub__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if (self._sign, other._sign) == ('+', '+'):
                    return self.__class__(*self._true_sub(self._fib_val, other._fib_val), is_fib_val=True)
                elif (self._sign, other._sign) == ('-', '-'):
                    return self.__class__(*self._true_sub(other._fib_val, self._fib_val), is_fib_val=True)
                return self.__class__(self._true_add(self._fib_val, other._fib_val), self._sign, is_fib_val=True)
            else:
                return None  # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            raise TypeError(f'can only subtract FibNum (not "{other.__class__.__name__}") from FibNum')
    def __isub__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if (self._sign, other._sign) == ('+', '+'):
                    self._fib_val, self._sign = self._true_sub(self._fib_val, other._fib_val)
                elif (self._sign, other._sign) == ('-', '-'):
                    self._fib_val, self._sign = self._true_sub(other._fib_val, self._fib_val)
                else:
                    self._fib_val = self._true_add(self._fib_val, other._fib_val)
            else:
                self = None  # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return self
        else:
            raise TypeError(f'can only subtract FibNum (not "{other.__class__.__name__}") from FibNum')

    def __mul__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if {self._sign, other._sign} == {'+', '-'}:
                    return self.__class__(self._true_mul(self._fib_val, other._fib_val), '-', is_fib_val=True)
                return self.__class__(self._true_mul(self._fib_val, other._fib_val), self._sign, is_fib_val=True)
            else:
                return None # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        else:
            raise TypeError(f'can only multiply FibNum (not "{other.__class__.__name__}") by FibNum')
    def __imul__(self, other):
        if isinstance(self, FibNum) and isinstance(other, FibNum):
            if self.__class__ == other.__class__:
                if {self._sign, other._sign} == {'+', '-'}:
                    self._fib_val, self._sign = self._true_mul(self._fib_val, other._fib_val), '-'
                else:
                    self._fib_val = self._true_mul(self._fib_val, other._fib_val)
            else:
                self = None  # дописать!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            return self
        else:
            raise TypeError(f'can only multiply FibNum (not "{other.__class__.__name__}") by FibNum')

    def __div__(self, other): ...
    def __idiv__(self, other): ...

    def __floordiv__(self, other): ...
    def __ifloordiv__(self, other): ...

    def __mod__(self, other): ...
    def __imod__(self, other): ...

    def __pow__(self, power, modulo=None): ...
    def __ipow__(self, other): ...

    def __eq__(self, other): ...
    def __ne__(self, other): ...
    def __lt__(self, other): ...
    def __gt__(self, other): ...

    def __pos__(self): ...
    def __neg__(self): ...

    def __abs__(self): ...
    def __round__(self, n=None): ...

    def __int__(self): ...
    def __float__(self): ...

    def __str__(self): ...
    def __repr__(self): ...

    def __len__(self): ...