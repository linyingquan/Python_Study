# 元类写法是固定的，必须继承自type，命名一般以MetaClass结尾
class TulignMetaClass(type):
    def __new__(cls, name, bases,attrs):
        #自己的业务处理
        print("我是元类")
        attrs['id'] = "00000"
        attrs['addr'] = "四川德阳"
        return type.__new__(cls, name, bases, attrs)
# 元类定义完就可以使用，使用注意写法
class Teacher(object,metaclass=TulignMetaClass):
    pass
# 使用
t = Teacher()
t.__dict__