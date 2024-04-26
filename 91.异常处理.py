"""
异常处理，可能出错看，不一定出错！
当程序出错之后还可以继续执行！
try except finally else
要根据异常的类型做处理！
Exception 可以捕获所有异常，一般位于最后一个。
如果没有出错！Try编写有可能出错的代码！
finally 不管程序是否出错！程序都会执行！
else 不出错才会执行else的语句！


raise 手动抛出一个指定异常！



"""


class OneDivisionError(Exception):
    def __init__(self, massage="在我的代码中！1不可以作为除数"):
        super().__init__()
        self.massage = massage


def divide(num, divisor):
    if divisor == 1:
        raise OneDivisionError()
    else:
        return num / divisor


try:
    # 有可能出错的代码！
    # print(1 + "0")
    # print("读取文件结束！")
    divide(2, 1)

except FileNotFoundError:
    print("读取文件出错！")

except ValueError:
    print("数值出错！")

except TypeError:
    print("类型出错！")
except IndexError:
    print("下标出错！")
except ZeroDivisionError:
    print("0不能作为除数！")

except OneDivisionError as e:
    print(e.massage)
# except Exception:
#     print("出错！")

else:
    print("并没有出错！")

# class OneDivisorError(Exception):
#     def __init__(self, message="除数不能为1"):
#         self.message = message
#         super().__init__(self.message)
#
#
# def divide(num, divisor):
#     if divisor == 1:
#         raise OneDivisorError()
#     else:
#         return num / divisor
#
#
# try:
#     result = divide(10, 1)
# except OneDivisorError as e:
#     print(e.message)
# else:
#     print(result)
