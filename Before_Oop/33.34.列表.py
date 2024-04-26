# l1 = [[[[[[[[[[[[1]]]]]]]]]]]]
#
# for e in l1:
#     print(e[0][0][0][0][0][0][0][0][0][0])
# l2 = [1, 0.21112, ["sd12rgt", 'fs1dgf', 'ws']]
# for e in l2:
#     print(e)
#
# print("")


def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fun(n):
    ans = []
    for i in range(1, n + 1):
        ans.append(fibonacci(i))
    return ans
# 1   1   2   3   5
print(fun(5))
