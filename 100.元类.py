"""
# 类的类型就是元类
"元类"
sds
"""
from typing import Type


# type()....
# MetaClass(


# class MetaClass(type):
#     def __new__(cls, class_name, base_name, attri_dict):
#         cls.class_name = "zh" + class_name
#         return super().__new__(cls, cls.class_name, base_name, attri_dict)
#
#
# Mc = MetaClass("MyClass", (), {})
# print(type(Mc), Mc.class_name)
class MetaClass(type):
    def __new__(cls, class_name, base_name, attri_dict):
        cls.class_name = "zh" + class_name
        cls.host = 'zh'
        return super().__new__(cls, cls.class_name, base_name, attri_dict)


Mc = MetaClass("MyClass", (), {})
print(type(Mc), Mc.class_name,Mc.host)
