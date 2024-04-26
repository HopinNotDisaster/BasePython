"""
线程执行没有先后顺序，谁抢到资源就是谁的
多个线程同时修改一个数据。

python是一门解释性的语言，
执行需要解释器解释，

在解释过程中，存在全局解释器
（GIL）global interpret lock（理论上[cpu级别上]同时只有一个线程在执行）！
所谓的多线程程序并不是同时执行的，在cpu级别上还是单个执行的

其他编程语言需要互斥锁来解决数据问题。
             interpret        解释！
I/O密集型 适合创建线程

# # 使用互斥锁，
# """
#
# import threading
#
# lock = threading.Lock()
#
# n = 0
#
#
# def add_n():
#     global n
#     for i in range(1000):
#         lock.acquire()
#         n += 1
#         lock.release()
#
#
# def main():
#     for i in range(2):
#         t = threading.Thread(target=add_n)
#         t.start()
#     print(n)
#
#
# if __name__ == '__main__':
#     main()


a = 5
print(id(a))
a+=1
print(id(a))
