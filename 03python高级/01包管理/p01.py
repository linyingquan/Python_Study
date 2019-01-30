# 包管理示例
class Student():
    def __init__(self, name="noname", age=18):
        self.name = name
        self.age = age
    def say(self):
        print("my name is {0}".format(self.name))

def sayhello():
    print("i am linyingquan")

# 此判断语句建议一直作为程序的入口
if __name__ == '__main__':
    print("this is python code")