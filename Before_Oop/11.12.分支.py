# 顺序结构

# print(1)print(1.1)报错
# print(1);print(1.2) 正确但一般不用


# 选择结构


#pass 
"""
if True:
    pass
    if 100 > 20:
        print("3.12")
        
if 100 > 50 and "" or 10:
    pass
    print("4")
    print(7)
    if 100 > 90:
        print("分支嵌套")
    if 1 > 2:
        print("0.0")
        

num1 = int(input("请输入一个数："))
if num1 % 2:
    num2 = int(input("请输入第一个数："))
    num3 = int(input("请输入第二个数："))
    if num2 > num3:
        print(num1 - num3)
        
if 10 > 50:
    pass

#  if 与 else 必须相邻 ，中间不可以有其他语句


# if  多分枝

if False:
    print("3.7")
else:
    print(7.3)
    if 100>89:
        print("2416")



num1 = int(input("请输入一个数字："))
if num1 % 5:
    num2 = int(input("请zai输入一个数字："))
    if num2 % num1:
        print("好好学习！")
    else:
        print("jixushui")
else:
    print("xingxingla")
    


value = 100
if value ==100:
    print("AAA")
elif value == 101:
    print("BBB")
else:
    print("CCC")


score = float(input("请输入成绩："))
if 100 >= score >= 90:
    print("优秀！")
elif 90 > score >= 75:
    print("良好！")
elif 75 > score >= 60:
    print("及格！")
elif 60 > score >= 0:
    print("渣渣！")
else:
    print("不合法！")
    

"""






















