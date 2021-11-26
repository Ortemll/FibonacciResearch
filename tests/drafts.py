import numpy as np


def correct_fib_val(value):
    separated_after = None
    while max(value) > 1:
        num = max(value)
        index = len(value) - value[::-1].index(num) - 1
        if len(value) < index + 3:
            if separated_after is None:
                separated_after = len(value) - 1
            value += [0] * (index + 3 - len(value))
        if index == 0:
            value = [num // 2, num % 2, value[1], value[2] + num // 2] + value[3:]
        else:
            value = value[:index - 1] + [value[index - 1] + num // 2, num % 2, value[index + 1],
                                         value[index + 2] + num // 2] + value[index + 3:]
        print(index, value)

    if len(value) > 1:
        while any([value[i] >= 1 and value[i + 1] >=1 for i in range(len(value) - 1)]):
            for i in range(len(value) - 1):
                if value[i] >= 1 and value[i + 1] >=1:
                    index = i
                    break
            val = min(value[i], value[i + 1])
            if index == 0:
                value = [val, value[0] - val, value[1] - val] + value[2:]
            else:
                value = value[:index - 1] + [int(value[index - 1]) + val, value[i] - val, value[i + 1] - val] + value[index + 2:]
            print(i, value)

    return value, separated_after


def dec_val(fib_val):
    value = 0

    fib_numbers = np.array((1, 2))
    matrix = np.array(((0, 1), (1, 1)))
    for power, _ in filter(lambda el: el[1] == '1', enumerate(fib_val[::-1], 0)):
        dot = np.dot(fib_numbers, np.linalg.matrix_power(matrix, power))
        # пибавляем полученное значение
        value += dot[0]

    return value


# num = abs(float(input()))
# start_point_numer, start_point_denom = 1, 1
# end_point_numer, end_point_denom = 1, 1
# x = (1, 1)
# while x[1] < num:
#    x = (x[1], sum(x))
# end_point_numer = x[1]
# mid_point_numer, mid_point_denom = start_point_numer + end_point_numer, start_point_denom + end_point_denom
# ans = lambda: mid_point_numer / mid_point_denom
# for _ in range(100):
#     if num == mid_point_numer / mid_point_denom:
#         break
#     elif num * mid_point_denom ** 2 > mid_point_numer ** 2:
#         start_point_numer, start_point_denom = mid_point_numer, mid_point_denom
#         mid_point_numer += end_point_numer
#         mid_point_denom += end_point_denom
#     else:
#         end_point_numer, end_point_denom = mid_point_numer, mid_point_denom
#         mid_point_numer += start_point_numer
#         mid_point_denom += start_point_denom
# print(mid_point_numer ** 2 - num * mid_point_denom ** 2)
# print(ans(),mid_point_numer, mid_point_denom)
