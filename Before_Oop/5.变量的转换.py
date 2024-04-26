# 整数变量 
i0 = 10
f0 = 3.14
f0 = int(f0)
s0 = "10"
s0 = int(s0)

s1 = "1010"
s1 = int(s1, 8)
s2 = "ff11"
s2 = int(s2, 16)

i1 = 100
i1 = float(i1)
print(i1, type(i1))

i1 = 15476e-4
print(i1, type(i1))

# # str()可以将任意数据类型转化为str
#
# b2 = False
# n2 = None
# print(len(str(b2)))
# n2 = str(n2)
# print(n2, type(n2))
# n3 = None
# print(n3, type(n3))
#
# # 负数转换为bool类型也为True
# i3 = 100
# i3 = bool(i3)
# i4 = -1
# i4 = bool(i4)
# print(i4)

def get_yinzi(n):
   l = []
   l1 = []
   for i in range(1, n + 1):
       if n % i == 0:
           l.append(i)
   for j in range(len(l)):
       if l[j] == 1:
           continue
       else:
           m = l[j]
           for k in range(2, m):
               if m % k == 0:
                   break
           else:
               l1.append(m)
   return l1


num = int(input("请输入一个正整数："))
get_yinzi = get_yinzi(num)
print(get_yinzi)