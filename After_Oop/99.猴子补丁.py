class People:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age


def set_age(self, age):
    self.age = age


p1 = People(18)
People.set_age = set_age
p1.set_age(20)
print(p1.age)

p2 = People(12)
p2.set_age(20)
print(p2.age)

# types.MethodType(新方法，给某个实例添加！)

# __slots__只能限制类本身，不可以限制子类！
# 优点！ 可以提高代码安全性！不需要再管之后会增添新的内容！
