class FibNum:
    def __init__(self):
        pass

    def make_value(self, value):
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
    def __int__(self, value):
        self.val = self.make_value(value)

    def make_value(self, value):
        pass


class FibFloat(FibNum):
    def __int__(self, value):
        self.val = self.make_value(value)

    def make_value(self, value):
        pass