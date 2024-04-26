#  第四题！
address = input("请输入地址：")
print("欢迎来到", address, sep="")
# {}可以回到python环境
# 格式化字符串   在字符串前加f


## 第五题！
username = input("请输入姓名：")
chinese = float(input("请输入语文成绩："))
math = float(input("请输入数学成绩："))
english = float(input("请输入英语成绩："))
total = (chinese + math + english)
avarage = total / 3
print(f"{username},你的总成绩为{total}分，平均成绩为{avarage}分")

# 7.接收用户输入的两个整数，存储到两个变量中，交换变量存储的值
