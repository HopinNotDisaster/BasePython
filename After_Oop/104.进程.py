"""
一个程序默认有一个主进程   一个进程默认有一个主线程
"""
# 进程数据！
import multiprocessing
import time


def worker(shared_value, number):
    while 1:
        time.sleep(3)
        print(f"进程{number}")
        shared_value += 1
        print(shared_value)


if __name__ == "__main__":
    # 创建进程
    shared_value = 0
    process1 = multiprocessing.Process(target=worker, args=(shared_value, 1))
    # 启动进程
    process1.start()
    process2 = multiprocessing.Process(target=worker, args=(shared_value, 2))
    # 启动进程
    process2.start()
    # 等待进程结束

