# 初次使用
- 时间：2019/1/27
- 作者：林应权 
- 使用markdown
  - 如果有链接在这里：https://www.cnblogs.com/bingabcd/p/8438627.html
使用python发邮件
  - 需要设置邮箱，需要授权码 ，不是很重要

# Python面向对象（oop）
- python的面向对象
- 面向对象编程
    - 基础
    - 公有私有
    - 继承
    - 组合，Mixin
- 魔法函数
    - 魔法函数概述
    - 构造类魔法函数
    - 运算类魔法函数   
# 1. 面向对象概述（ObjectOriented）
- OOP思想
    - 接触到任意一个任务，首先想到的是任务这个世界的构成，是由模型构成的
- 几个名词
    - OO : 面向对象
    - OOA : 面向对象分析
    - OOD : 面向对象设计 
    - OOI : 面向对象实现
    - OOP : 面向对象编程
    - OOA -> OOD -> OOI : 面向对象的实现过程  
    
- 类和对象的概念
    - 类 ：抽象名词，代表一个集合，共性的事物
    - 对象 ：具体的事物，单个个体
    - 类与对象的关系
        - 一个具象，代表一类事物或某一个个体
        - 一个抽象，代表的是一大类事物
- 类中的内容，应该具有两个内容
    - 表明事物的特征，叫做属性（变量）
    - 表明事物功能或者动作，成为成员方法（函数）
    
# 2. 类的基本实现
- 类是命名
    - 遵守变量命名规范
    - 大驼峰（有一个或者多个单词构成，每个单词首字母大写，单词跟单词直接相连）
    - 尽量避开跟系统命名相似的命名
- 如何声明一个类
    - 必须用class关键字
    - 类由属性和方法构成，其他不允许出现
    - 成员属性定义可以直接使用变量赋值，如果没有值，可以使用None
    - 例如 01.py
- 实例化类
    
        变量 = 类名（） #实例化了以一个类
        
- 访问对象成员
    - 使用点操作符
    
            obj.成员属性名
            obj.成员方法
- 可以通过默认内置变量检查类和对象的所有成员
    - 对象所有成员检查
    
            # dict前后各有两个下划线
            obj.__dict__
            
    
# 3. anaconda基本使用
- anaconda主要是一个虚拟环境管理器
- 还是一个安装包管理器
- conda list ： 显示anaconda安装的包（Linux环境）
- conda env list : 显示anaconda的虚拟环境列表
- conda create -n xxx python=3.6  : 创建一个python版本为3.6的虚拟环境，名称为xxx

# 4. 类和对象的成员分析
- 类和对象都可以存储成员，成员可以归类所有，也可以归对象所有
- 类存储成员时使用的是与类关联的一个对象
- 独享存储成员是存储在当前对象中的
- 对象访问一个成员时，如果对象中没有该成员，尝试访问类中的同名成员，如果对象中有此成员，一定使用对象中的成员
- 创建对象的时候，类中的成员不会放入对象中，而是得到一个空对象，没有成员
- 通过对象对类中的成员重新赋值或者通过对象添加成员时，对于成员会保存在对象中，而不会修改类成员
- 图例1，2

# 5. 关于self
- self在对象中的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中
- self不是关键字，只是一个用于接受对象的普通参数，理论上可以用任何一个普通变量名代替
- 方法中有self形参的方法成为非绑定类的方法，可以通过对象访问，没有self的是绑定类的方法，只能通过类访问
- 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过__class__成员名来访问

# 6. 面向对象的三大特性
- 封装
- 继承
- 多态

## 6.1 封装
- 封装就是对对象的成员进行访问限制
- 封装的三个级别：
    - 公开，public
    - 受保护的，protected
    - 私有的，private
    - public，private，protected不是关键字
- 判别对象的位置
    - 对象内部
    - 对象外部
    - 子类中
- 私有
    - 私有成员是最高级别的封装，只能在当前类或对象中访问
    - 在成员前面添加两个下划线即可，如：
    
            class Pi():
                # name是公有成员
                name = "lin"
                # __age就是私有成员
                __age = 18
                
    - python的私有不是真私有，是一种称为name mangling的改名策略，可以使用对象 `._类名_age` 还是可以访问的
- 受保护的封装 protected
    - 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以进行访问，但是在外部不可以
    - 封装方法：在成员名称前添加一个下划线即可
- 公开的 public
    - 公共的封装实际对成员没有任何操作，任何地方都可以访问
    
## 6.2 继承
- 继承就是一个可以获得另外一个类中的成员属性和成员方法
- 作用： 减少代码，增加代码的复用功能，同时可以设置类与类直接的关系
- 继承与被继承的概念：
    - 被继承的类叫父类，也叫基类，也叫超类
    - 用于继承的类，叫子类，也叫派生类
    - 继承与被继承一定存在一个 is-a 关系
    
            #继承的语法
            #在python中，任何类都有一个共同的父类叫object
            class Person():
                name = "noname"
                age = "0"
                def sleep(self):
                    print("sleeping......")
                    
            class Teacher(Person):
                pass
                
    - 继承的特征
        - 所有的类都继承自object类，即所有的类都是object类的子类 
        - 子类一旦继承父类，则可以使用父类中除私有成员外的所有内容
        - 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
        - 子类中可以定义独有是成员属性和方法
        - 子类中定义成员和父类成员如果相同，则优先使用子类成员
        - 子类如果想扩充父类的方法，可以在定义新方法的同时访问父类成员来进行代码重用，
        可以使用 ` 父类名.父类成员 ` 的格式来调用父类成员也可以使用super（）.父类成员的格式来调用
    - 继承变量函数的查找顺序问题
        - 优先查找自己的变量
        - 没有则查找父类
        - 构造函数如果本类中没有定义，则自动查找调用父类构造函数
        - 如果本类有定义，则不在继续向上查找
    - 构造函数
        - 是一类特殊的函数，在类进行实例化之前进行调用
        - 如果定义了构造函数，则实例化时使用构造函数，不查找父类构造函数
        - 如果没有定义，则自动查找父类构造函数
        - 如果子类没定义，父类的构造函数带参数，则构造对象时的参数应该按父类参数构造
        
                #构造函数的概念1
                class Dog():
                   # __init__就是构造函数
                   # 每次实例化的时候，第一个被调用
                   # 因为主要工作是进行初始化，所以得名
                   def __init__(self):
                        print ("i an init in dog")

                kaka  = Dog()
                 
                 
                输出结果： i an init in dog




        
                #构造函数的概念2
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
                    
                kaka = Dog()
                caca = Cat()
        
                
                输出结果：
                i an init in dog
                burudwu
- super
    - super不是关键字，而是一个类
    - super的作用是获取 MRO （MethodResolutionOrder）列表中的第一个类
    - super于父类没有任何实质性关系，但通过super可以调用到父类
    - super使用两个方法，参见在构造函数中调用父类的构造函数
    
- 单继承和多继承
    - 单继承：每个类只能继承一个类
    - 多继承：每个类允许继承多个类
- 单继承和多继承优缺点
    - 单继承：
        - 继承有序逻辑清晰，语法简单，隐患少
        - 功能不能无限扩展，只能在当前唯一的继承链中扩展
    - 多继承：
        - 类的功能拓展方便
        - 缺点继承关系混乱
## 6.3 多态
- 多态就是同一个对象在不同情况下有不同的状态出现
- 多态不是语法，是一种设计思想
- 多态性：一种调用方式，不同的执行结果
- 多态：同一事物的多种形态，动物分为狗类，猪类，
- 参考文档：

- Mixin设计模式
    - 主要采用多继承方式对类的功能进行扩展
    - 参考文档：
    
- 我们使用多继承语法来实现Minxin
- 使用Mixin实现多继承的时候非常小心
    - 首先他必须表示某一单一功能，而不是某个物品
    - 职责必须单一，如果由多个功能，则写多个Mixin
    - Mixin不能依赖于子类的实现
    - 子类及时没有继承Mixin类，也能照样工作，只是缺少了某个功能
- 优点：
    - 使用Mixin可以在不对类进行任何修改的情况下扩充功能
    - 可以方便的组织和维护不同功能组件的划分
    - 可以避免创建很多新的类，导致类的继承混乱
    
## 6.4 类相关函数
- issubclass：检测一个类是否是一个类的子类
- isinstance：检测一个对象是否是一个类的实例
- hasattr：检测一个对象是否有属性xxx
- getattr： get attribute
- setattr： set attribute
- delattr： delattr attribute
- dir: 获取对象的成员列表

# 7 类的成员描述符（属性）
- 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
    - get：获取属性的操作
    - set：修改或添加属性操作
    - delete：删除的操作
- 属性的三种用法：
    - 赋值
    - 读取
    - 删除
- 使用类的成员描述符，有三种方法：
    - 使用类实现描述器
    - 使用属性修饰符
    - 使用property函数
        - property函数比较简单
        - property（fget，fset，fdel，doc）

        
     #使用函数改变属性
     '''
     属性的使用示例
     创建Student类，描述学生
     学生具有Student.name属性
     但name格式并不统一
     可以用增加一个函数，然后自己调用的方式，但很蠢
     '''
        class Student():
            def __init__(self,name,age):
                self.name = name
                self.age = age
                
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
     
    输出结果：
    hai,my name is LIN
    hai,my name is AOXI
    
- 使用property函数改变属性
        
        #使用property函数改变属性
        '''
        定义一个person的类，具有name，age两个属性
        对于任意输入的姓名，我们希望都用大写方式保存
        年龄，我们希望统一用整数保存
        x = property（fget，fset，fdel，doc）
        '''
        class Person():
            # 此功能，是对类变量进行读取操作的时候应该执行的函数功能
            def fget(self):
                return self._name * 2
            # 模拟的是对变量进行写操作的时候执行的功能
            def fset(self,name):
                self._name = name.upper()
            # 模拟的是删除变量的时候进行的操作
            def fdel(self):
                self._name = "noname"
            # property的四个参数是固定的
            name = property(fget,fset,fdel,"说明")

        p1 = Person()
        p1.name = "lin"
        print(p1.name)
        
        输出结果：
        LINLIN
     
## 7.1 类的内置属性
    __dict__ ： 以字典的方式显示类的成员组成
    __doc__ ： 获取类的文档信息
    __name__ ： 获取类的名称，在模块中使用则获取模块的名称
    __bases__： 获取某个的所有父类，以元组方式显示    
    
# 8. 类的常用魔术方法
- 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发 
- 魔术方法的统一特征，方法名被前后各两个下划线包裹
- ` __init__ `:构造函数就是典型的魔术方法
- ` __new__`:对象实例化方法，此函数比较特殊，一般不需要使用
- ` __call__ `:对象当函数使用时触发

        #__call__示例
        class A():
            def __init__(self,name = 0):
                print("hahaha")
            def __call__(self):
                print("我被调用了")
        a = A()
        a()  #把对象当作函数调用
        
        输出结果：
        hahaha
        我被调用了
- 更多魔法函数可参考：https://tulingxueyuan.gitbooks.io/python/content/docs/2%E3%80%81Python%E9%AB%98%E7%BA%A7/%E9%AD%94%E6%B3%95%E5%87%BD%E6%95%B0%E6%A6%82%E8%BF%B0.html

# 9. 类和对象的三种方法
- 实例方法
    - 需要实例化对象才能使用的方法，使用过程中可能需要截止对象的其他对象的方法完成
- 静态方法
    - 不需要实例化，通过类直接访问
- 类方法
    - 不需要实例化
- 代码示例：

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

            # 静态方法，不需要用第一个参数表示自身或类
            @staticmethod
            def say():
                print("saying...")

        lin = Person()

        # 实例方法
        lin.eat()
        # 类方法
        Person.play()
        lin.play()
        # 静态方法
        Person.say()
        lin.say()
        
        输出结果：
        <__main__.Person object at 0x0000011963DF85C0>
        eating...
        <class '__main__.Person'>
        playing...
        <class '__main__.Person'>
        playing...
        saying...
        saying...
        
# 10. 抽象类（软件工程类）
- 抽象方法：没有具体实现内容的方法称为抽象方法
- 抽象方法的主要意义是规范子类的行为和接口
- 抽象类的使用需要借助abc模块

        import abc
    
- 抽象类：包含抽象方法的类叫抽象类，通常称为abc类
- 抽象类的使用
    - 抽象类可以包含抽象方法，也可以包含具体方法
    - 抽象类中可以有方法也可以有属性
    - 抽象类不允许直接实例化
    - 必须继承才能使用，且继承的子类必须实现所有继承来的抽象方法
    - 假定子类没有实现所有继承的抽象方法，则子类也不能实例化
    - 抽象类的主要作用是设定类的标准，以便于开发的时候有统一的规范
    - 使用示例:
    
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
                # 普通的具体方法
                def sleep(self):
                    print("sleeping...")

# 11. 自定义类
- 类其实是一个类定义和各种方法的组合
- 可以定义类和函数，然后自己通过类直接赋值

        # 自己组装一个类
        class A():
            pass

        def say(self):
            print("123aaa")

        say(1)
        # 函数名当作变量用
        A.say = say
        a = A()
        a.say()
        
        输出结果：
        123aaa
        123aaa
        
- 可以借助MethodType实现

        # 通过MethodType组装一个类
        from types import MethodType
        class A():
            pass
            
        def say(self):
            print("123aaa")
        
        a = A()
        a.say = MethodType(say,A)
        a.say()
        
- 借助于type实现

        # 通过type组装一个类
        # 先定义类应该具有的成员函数
        def say(self):
            print("123aaa")
        def talk(self):
            print("talking...")
        # 用type来创建一个类，详细使用方法help（type）
        A = type("Aname",(object,),{"class_say":say,"class_talk":talk})
        # 然后可以正常访问此类
        a = A()
        a.class_say()
        a.class_talk()
        
        输出结果：
        123aaa
        talking...
        
- 利用元类实现 MetaClass
    - 元类是类
    - 用来创建别的类，元类的写法是固定的，必须继承自type
    
    
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