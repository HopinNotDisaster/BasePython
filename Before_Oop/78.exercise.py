import numpy as np

# np是个类！
array = [
    [1, 2, 3, ],
    [2, 3, 4, ]
]
np_arr = np.array(array)  # 调用np里面的array方法，返回一个np专有的矩阵数据类型

# print(np_arr)
# print(type(np_arr))
# print("number of dim:", np_arr.ndim)
# print(np_arr.min(initial=None))
# print(np_arr > 2)
# 数组不等号数字时，会返回一个形状相同的数组，里面存放True或者False，就是将数组中的每一个
# 元素与该数字进行比较的每个结果！

arr_1 = np.array([1, 2, ])
# print(arr_1)
arr_2 = np.arange(1, 10)
arr_3 = np.zeros(10)
arr_4 = np.ones((2, 3), dtype="int32")
# print(arr_4, arr_4.dtype)
# print(arr_3, arr_3.dtype)
arr_5 = np.ones(5, ) / 5
# print(arr_5)
print(np.zeros_like(arr_4))
# 像就是维度像。

