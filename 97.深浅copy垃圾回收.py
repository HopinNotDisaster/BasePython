"""
研究的都是可变类型！
1. = 赋值 直接使用原始地址，修改一个，另一个跟着改变！
2. 浅拷贝 外层copy值，内层copy地址！
3. 深拷贝  好理解 ，全都不一样！！！
"""
l0 = [0, 1, 2]
l1 = l0.copy()
l1[0]=5
print(id(l0[0]), id(l1[0]))
print(l0[0])
# import copy
# # 创建原始列表
# original_list = [1, 2, 3, 4]
# # 进行浅拷贝
# new_list = copy.copy(original_list)
# # 修改新列表中的元素
# new_list[0] = 99
# print(id(original_list[0]))  # 输出原始列表
# print(id(new_list[0]))  # 输出新列表
# 引用计数
# 循环标记
# 标记清除与分代收集   标记越高越先回收!强行回收！

# import sys

# x = 10000
# print(sys.getrefcount(10000))
