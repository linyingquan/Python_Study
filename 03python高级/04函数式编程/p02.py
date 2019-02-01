# 装饰器案例
# 功能说明：对hello函数进行功能扩展，每次执行hello前打印当前时间
# 以下代码为装饰器的固定写法
import time

def printTime(f):
    def wrapper( *args, **kwargs):
        print("Time:",time.ctime())
        return f( *args, **kwargs)
    return wrapper

@printTime # 被装饰器装饰过的函数都会先进行装饰函数里的内容，然后执行下面函数的内容
def hello():
    print ("hello word!")

hello()

@printTime
def lin():
    print("123saasxd")
    print("abcdefg")

lin()

# 手动执行
def lin2():
    print("我是手动执行的")

lin2()
print("*"*20)
lin2 = printTime(lin2)
lin2()
print("*"*20)
a = printTime(lin2)
a()

