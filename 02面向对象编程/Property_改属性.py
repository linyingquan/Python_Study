'''
定义一个person的类，具有name，age两个属性
对于任意输入的姓名，我们希望都用大写方式保存
年龄，我们希望统一用整数保存
x = property（fget，fset，fdel，doc）
'''
class Person():
    # 函数名称可以任意取
    def fget(self):
        return self._name * 2

    def fset(self,name):
        self._name = name.upper()

    def fdel(self):
        self._name = "noname"

    name = property(fget,fset,fdel,"对name进行以下操作")

p1 = Person()
p1.name = "lin"
print(p1.name)