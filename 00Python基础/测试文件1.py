'''
这是一个python测试文件
'''
#构造函数的概念

class Animel():
    pass
class BuruAni():
    def __init__(self):
        print("burudwu")

class Dog(BuruAni):
    # __init__就是构造函数
    # 每次实例化的时候，第一个被调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print ("i an init in dog")

class Cat(BuruAni):
    pass

kaka  = Dog()
c = Cat()
