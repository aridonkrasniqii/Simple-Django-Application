import time
import threading

""" Without threading """


def func():
    print('Start')
    time.sleep(10)
    print('End')


# for _ in range(5):
#     func()

""" With threading """


def func():
    print('Start')
    time.sleep(10)
    print('End')


for _ in range(5):
    thread1 = threading.Thread(target=func)
    thread1.start()

# This will print the amount of thread
# And it will be 6 because python will launch a thread in the beginning of the program which is main thread
print(threading.active_count())
