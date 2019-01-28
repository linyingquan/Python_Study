'''
定义一个学生类，用来形容学生
'''
# 定义一个空的类
class Student():
    pass  # pass代表直接跳过

# 定义一个对象
linquan = Student()

# 再定义一个类，用来描述听python的学生
class PythonStudent():
    # 用None给不确定值赋值
    name = None
    age = 8
    course = "python"

    #需要注意：1. def doHomework的缩进
    #2.系统默认有一个self参数
    def doHomework(self):
        print("在做作业")
        # 推荐在函数末尾使用return语句
        return None
# 定义一个叫laownag的学生
laowang = PythonStudent()
print(laowang.age)
print(laowang.name)
# 调用成员函数不用带参数
laowang.doHomework()
