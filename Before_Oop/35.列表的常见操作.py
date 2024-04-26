# 追加
# #      pop 删除一个，可
# l = [0.12, 12, 55, 'we1r']
# print(id(l))
# l.pop()
# print(l, id(l))
# l.clear()
# print(l)
# l = [1,2,3]
# print(l.index(3))
#
#
# l = [1, 351, 315, 351, 1, 3132, 312315, 315, 351, 351, ]
# l.sort()
# print(l)

import random

l = []
max_value = random.randint(10, 100)
l.append(max_value)
min_value = max_value
n = 49
while n:
    tem = random.randint(10, 100)
    l.append(tem)
    # if tem > max_value:
    #     max_value = tem
    # if tem < min_value:
    #     min_value = tem
    n -= 1
l.sort()
print(f"最大值与最小值的差为：{l[49] - l[0]}")
print(max(l), min(l))
# print(max_value, min_value)
print(l)
