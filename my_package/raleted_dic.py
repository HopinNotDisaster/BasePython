def my_max(dics):
    """
    传入一个列表，列表元素全是字典，
    且字典中需要有value的键且值为int型
    :param dics:
    :return:返回value值最大的字典
    """
    return max(dics, key=lambda e: e["value"])
