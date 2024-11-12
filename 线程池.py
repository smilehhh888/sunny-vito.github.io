# 一次性开辟一些线程，我们用户直接给线程池子提交任务 线程任务的调度交给线程池来完成
# from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# def fn(name):
#     for i in range(1000):
#         print(name,i)
# if __name__ == '__main__':
#     # 创建线程池
#     with ThreadPoolExecutor(50) as t: # 创建由50个线程组成的线程池
#         for i in range(100):
#             t.submit(fn,name=f"线程{i}")
#
#     print("123") # 等待线程池子中的任务全部执行完毕，才继续执行(守护)


from threading import Thread
from concurrent.futures import ThreadPoolExecutor
def func(name):
    for i in range(10000000):
        print(name ,i)
if __name__ == '__main__':
    with ThreadPoolExecutor(50) as t:
        for i in range(1000):
            t.submit(func,name=f"线程{i}")
