# 高阶函数示例

# funA是普通函数，返回传入数值的100倍
def funA(n):
    return n * 100

# 再写一个函数，把传入参数乘以300倍，
def funB(n ):
    # 最终是想返回300n
    return funA(n) * 3

print(funB(9))

# 写一个高阶函数
def funC(n, f):
    # 假定函数是把n扩大100被
    return f(n) * 3

print( funC(9, funA) )

# 比较funC和funB, 显然funC的写法要优于funB
# 例如：
def funD(n):
    return n*10

# 需求变更，需要把n放大三十倍，此时funB则无法实现
print(funC(7, funD))