#抽象类的实现
import abc
class Human(metaclass=abc.ABCMeta):
    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass
    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass
    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(self):
        print("sleeping...")
