# 列表生成式

# 列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。

# 举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 可以用list(range(1, 11))：

list = list(range(1, 11))
print(list)

# 成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

# 对上面的写法 换成 列表生成式
list = [x * x for x in range(1, 11)]
print(list)

# 使用两层循环，进行全排列
list = [m + n for m in 'ABC' for n in 'XYZ']
print(list)

# 运用列表生成式，可以写出非常简洁的代码。
# 例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os  # 导入os模块,这个import应该放到顶部

list = [d for d in os.listdir('.')]  # os.listdir可以列出文件和目录
print(list)

# for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和
d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, "=", v)

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C'}
list = [k + "=" + v for k, v in d.items()]
print(list)

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，
# 所以列表生成式会报错：
# 使用内建的isinstance函数可以判断一个变量是不是字符串：
# 请修改列表生成式，通过添加if语句保证列表生成式能正确地执行：
L1 = ['Hello', 'World', 'Apple', 18, None]
L2 = [s.lower() for s in L1 if isinstance(s, str)]
print(L1 == L2)
# 测试
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
