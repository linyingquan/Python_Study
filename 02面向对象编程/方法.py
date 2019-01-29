'''
类和对象的三种方法案例
'''
class Person():
    def eat(self):
        print(self)
        print("eating...")

    # 类方法,类方法的第一个参数，一般为cls
    @classmethod
    def play(cls):
        print(cls)
        print("playing...")

    #静态方法，不需要用第一个参数表示自身或类
    @staticmethod
    def say():
        print("saying...")

lin = Person()

# 实例方法
lin.eat()
print("*"*10)
# 类方法
Person.play()
print("#"*15)
lin.play()
print("@"*10)
# 静态方法
Person.say()
lin.say()