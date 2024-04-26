# +-*/
# %  求余！
num1 = 10
num2 = 3
print(f"{num1}%{num2} = {num1%num2}")
# 求余经常会判定奇偶

## **幂运算
print(f"{num1}**{num2} = {num1**num2}")
# m**n表示m的n次方
# // 表示整除 结果为int类型
print(f"{num1}/{num2} = {num1/num2}")

i = num1//num2
print(i, type(i))
print(f"{num1}//{num2} = {num1//num2}")

# 优先级

print(2-1*5)

# ** 高于 //

# 比较运算符的结果是bool
# > < >=  <=  !=  == 

# 类型不一样结果为False
#  But int的0等于bool的False  int的1等于bool的True
print(200==True, 200==False)# 200不是bool类型，结果均为False
  
# python中可以使用连续比较
print(5>3>1)

# 算术运算符比比较运算符的优先级要高
# 比较运算符的优先级要高于赋值运算符





# 逻辑运算符
# and 逻辑与  （串联）
# and的结果不是True和False

ret = "0" and 100
print(ret) # 返回100

Ret = 1 and 5>3
print(Ret) # 返回True

# or 
# r = 0 or 0
# print(r)

# not

# result = not 0
# print(result)

# 位运算符
# 按位与    &

# a = 0b10101
# b = 0b10110
#     00011=3
#  &  10100=20

# print(a^b)
# ^ 异或
#  >> 右移23
# a = 10
# print(a<<1)









