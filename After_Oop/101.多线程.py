"""
默认系统都会有一个主线程
while 1 可以阻塞主线程
浪费os资源！
多个线程之间互不影响，相互独立！
"""

#
# def fun(i):
#     while 1:
#         print(i)
#
#
# import threading
#
# if __name__ == '__main__':
#     t_list = []
#     for i in range(5):
#         t = threading.Thread(target=fun, args=(i,))
#         t_list.append(t)
#
#     for i in range(5):
#         t_list[i].start()
#
#     for i in range(5):
#         t_list[i].join()
#
#     print("主线程结束！")


import random

templ = []
count = 0
while True:
    count += 1
    tem_num = random.randint(101, 200)
    if tem_num not in templ:
        templ.append(tem_num)
    if len(templ) == 50:
        break
print(count)
# print(len(templ))
