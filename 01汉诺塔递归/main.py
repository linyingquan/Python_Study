# 汉诺塔递归调用
def hano(n,a,b,c):
    '''
    汉诺塔递归调用函数
    将a上面的盘子移动到c上面，
    保证大盘子不能放在小盘子下，
    每次只能移动一个盘子
    :param n: 代表有几个盘子
    :param a: 代表第一个盘子，开始的盘子
    :param b: 代表第二个盘子，过渡盘子
    :param c: 代表第三个盘子，目标盘子
    :return: 结束状态
    '''
    if n == 1:
        print(a,"->",c)
        return None
    if n == 2:
        print(a,"->",b)
        print(a,"->",c)
        print(b,"->",c)
        return None
    # 把n-1个盘子，从a移动到b，借助于c
    hano(n-1,a,c,b)
    print(a,"->",c)
    # 把n-1个盘子，从b移动到c，借助于a
    hano(n-1,b,a,c)

a = "a"
b = "b"
c = "c"
n = 2
hano(n,a,b,c)
