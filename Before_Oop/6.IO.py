# # 输入与输出
#
# print(1, 3.14, "hello", False)
# print(1, 3.14, "hello", False, sep="*****")
# # 通过sep指定分隔符号时，必须写在最后
# print(1, end="666")
# print(1, 3.14, "hello", False, sep="*****", end="3.7")
# print()
# # 输入
# in_str = input("开始输入内容:")
# print("你输入的内容是:", in_str, type(in_str))
# print("程序运行结束")
#
# # 输入五个数，计算五个数的平均数
# a = float(input("输入第一个数："))
# b = input("输入第二个数：")
# c = input("输入第三个数：")
# e = input("输入第四个数：")
# f = input("输入第五个数：")
# b = float(b)
# c = float(c)
# f = float(f)
# e = float(e)
# Sum = float(a + b + c + e + f)
# print(Sum / 5)
import json


class People:
    def __init__(self, age, sex):
        self.age = age
        self.sex = sex


class MyJsonEncode(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, People):
            return f"年龄：{o.age}性别：{o.sex}"
            # print("一个人类~！")


class MyJsonDecode(json.JSONDecoder):
    def decode(self, s):
        # "算一个字符！
        # print(s[0], type(s))
        age = int(s[4:6])
        sex = s[-1]
        return People(age, sex)
        # return s


p0 = People(18, '女')
s0 = json.dumps(p0, cls=MyJsonEncode, ensure_ascii=False)
print(s0, type(s0))
p00 = json.loads(s0, cls=MyJsonDecode)
print(p00, type(p00))
