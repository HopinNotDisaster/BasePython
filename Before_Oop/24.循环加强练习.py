# n1 = int(input("输入："))
# n2 = int(input("输入："))
# ans1 = max(n1, n2)
# while 1:
#     if ans1 % n1 == 0 and ans1 % n2 == 0:
#         print(ans1)
#         break
#     ans1 += 1
# ans2 = min(n1, n2)
# while 1:
#     if n1 % ans2 == 0 and n2 % ans2 == 0:
#         print(ans2)
#         break
#     ans2 -= 1

for i in range(500, 1000):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)

