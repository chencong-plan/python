# 迭代
# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。

# 判断对象是否是可迭代对象，方法是通过collections模块的Iterable类型判断：

from collections import Iterable

a = isinstance('abc', Iterable)
b = isinstance([1, 2, 3], Iterable)
c = isinstance(123, Iterable)
print("str是否可迭代", a)
print("list是否可迭代", b)
print("整数是否可迭代", c)

# 如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身
list = ['A', 'B', 'C']
for i, value in enumerate(list):
    print((i, value))

# 上面代码当中我们引入了两个变量，下面也可以

for x, y in [(1, 2), (3, 4), (5, 6)]:
    print(x, y)


# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if len(L) == 0:
        return None, None
    min = L[0]
    max = L[0]
    for temp in L:
        if temp > max:
            max = temp
        if temp < min:
            min = temp
    return min, max


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
