print('1100921 1 11'.find('11'))

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
