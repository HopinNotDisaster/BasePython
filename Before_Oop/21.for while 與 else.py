# for i in range(10):
#     if i == 90:
#         break
#     print(i)
# else:
#     print("完整结束！")


#
# count = 0
# for i in range(2, 1000):
#     if count == 10:
#         break
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         count += 1
#         print(i)
#
# for i in range(2, 2):
#     print(i)
#
# num = 11
# i = 2
# while i < 9:
#     if num % i == 0:
#         print("不是质数！")
#         break
#     i += 1
# else:
#     print("是")

count = 10
i = 999
while count:
    j = 2
    while j < i:
        if i % j == 0:
            i -= 1
            break
        else:
            j += 1
    else:
        print(i)
        i -= 1
        count -= 1
