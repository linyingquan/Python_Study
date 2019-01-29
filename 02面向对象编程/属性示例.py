'''
属性的使用示例1
创建Student类，描述学生
学生具有Student.name属性
但name格式并不统一
可以用增加一个函数，然后自己调用的方式，但很蠢
'''
class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

        # 如果不想修改代码
        self.setName(name)
    # 介绍自己
    def intro(self):
        print("hai,my name is {0}".format(self.name))
    def setName(self,name):
        self.name = name.upper()

s1 = Student("Lin",18)
s2 = Student("aoxi",20)

s1.intro()
s2.intro()

