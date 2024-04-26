# 顺序结构
# 分支结构
# 循环结构： 重复多次执行！


for i in range(98, 103):
    print(f"{i}下雪啦！")

for i in ["xxla!!", "123456", "!!!", 56]:

    print(i)
    if str(type(i)) == "<class 'str'>":
        for j in i:
            print(j)

"""
total = 0
n = 0
for i in range(500, 1001):
    if n == 10:
        break
    if i % 13 == 0:
        total += i
        n += 1
print(total/n)




total = 0
n = 0
for i in range(500, 1001):
    if n == 10:
        break
    if i % 5 == 0:
        total += i
        n += 1
print(total/n)
"""