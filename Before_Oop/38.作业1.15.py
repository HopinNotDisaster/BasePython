# 1.计算二维列表中所有数字的平均数
# [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]

# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# l0 = []
# for i in arr:
#     for j in i:
#         l0.append(j)
# print(f"这10个数的平均数为：{sum(l0) / len(arr) ** 2}")
# print(l0)

# 2.编写一个程序，输入一个字符串，统计其中每个字符出现的次数
# s = input("输入：")
# ans = []
# for i in s:
#     for j in ans:
#         if j[0] == i:
#             j[1] += 1
#             break
#     else:
#         ans.append([i, 1])
# print(ans)

# # 3.实现二维数组的转置
#
# arr = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i > j:
#             arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
# print(arr)

# # 4.编写一个程序，输入一个列表和一个整数 n，将该列表中的所有元素都循环右移 n 位，并输出修改后的列表。
#
# lst = [" a","b","c","d","e"]
#        # e   d   c   b   a
#        # d   e
#        #         a   b   c
# # n = int(input("输入："))
# n= 2
# # lst = input("请输入一个列表，各个元素之间用空格隔开：").split()
# print("输入的列表为：", lst)
# lst = lst[::-1]
# lst1 = lst[0:n]
# lst2 = lst[n:]
# lst1 = lst1[::-1]
# lst2 = lst2[::-1]
# lst1.extend(lst2)
# print(lst1)

# # n = int(input("输入："))
# # lst = input("请输入一个列表，各个元素之间用空格隔开：").split()
# n= 2
# lst = ["a","b","c","d","e"]
# print("列表为：", lst)
# lst = lst[::-1]
# print(lst)

# lst1=lst[n-1:-1:-1]
# # lst1=[]
# # lst1.extend(lst[n-1:-1:-1])
# print(lst1)
# # lst2 = lst[n:]
# # lst1 = lst1[::-1]
# # lst2 = lst2[::-1]
# # lst1.extend(lst2)
# # print(lst1)

# # 5.找出一个二维数组每行的最大值
# # [
# #     [1, 5, 9],
# #     [2, 3, 6],
# #     [7, 5, 3]
# # ]
# # 输入 9 6 7
# #
# arr = [
#     [1, 5, 9],
#     [2, 3, 6],
#     [7, 5, 3]
# ]
# for i in arr:
#     print(max(i))

# 6.找出一个二维数组每列的最大值
# [
#     [1, 5, 9],
#     [2, 3, 6],
# [7, 5, 3]
# ]
# 输入 7 5 9

# arr = [
#     [1, 5, 9,100],
#     [2, 3, 6,200],
#     [7, 5, 3,3]
# ]
# for i in range(len(arr[0])):
#     max_v = arr[0][i]
#     for j in range(1, len(arr)):
#         if arr[j][i] > max_v:
#             max_v = arr[j][i]
#     print(max_v)

# 7.对二维数组进行水平镜像
# [
# [1,2,3],
# [4,5,6],
# [7,8,9]
# ]
# #
# arr = [
#     [3, 2, 1],
#     [6, 5, 4],
#     [9, 8, 7]
# ]
#
# for i in range(len(arr)):
#     arr[i] = arr[i][::-1]
# print(arr)
# # # 19.对二维数组进行竖直镜像
# # # [
# # [1,2,3],
# # [4,5,6],
# # [7,8,9]
# # ]
# #
# # [
# # [7,8,9],
# # [4,5,6],
# # [1,2,3]
# # ]

# l0 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# ans = [[0] * 3 for i in range(3)]
#
# for i in range(len(l0)):
#     for j in range(len(l0[i])):
#         ans[len(l0) - i - 1][j] = l0[i][j]
# print(ans)

# # 20.自己编写方法对列表进行升序排列
# # [10,50,20,60,40,30]
# l0 = [10, 50, 20, 60, 40, 30]
# p = 1
# while p < len(l0):
#     q = p - 1
#     while q >= 0:
#         if l0[q] <= l0[q + 1]:
#             break
#         else:
#             tem = l0[q]
#             l0[q] = l0[q + 1]
#             l0[q + 1] = tem
#             q -= 1
#     p += 1
# print(l0)

ans_dic = {

}


def fun(s):
    for i in s:
        if i in ans_dic:
            ans_dic[i] += 1
        else:
            ans_dic[i] = 0
    return max(ans_dic, key=ans_dic.get)


print(fun("agagaaas"))
