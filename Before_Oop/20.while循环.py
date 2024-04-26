# x = 1
# while x:
#     print(x)
#     x -= 1
#
# while 123:
#     print(123)
# pass
#
# n = 10
# while n:
#     print("xxl")
#     n -= 1
#
# import random
#
# count = 0
# total = 0
# while total <= 100:
#     count += 1
#     total += random.randint(5, 10)
#     print(total)
# print(count)

rank = 1  # 列
line = 1  # 行
while line < 10:
    rank = 1
    while rank < 10:
        if rank + line >= 10 and line >= rank or rank + line <= 10 and line <= rank:
            print(" * ", end="")
        else:
            print("   ", end="")
        rank += 1
    line += 1
    print()
