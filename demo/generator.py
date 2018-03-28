# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

# 所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

# 要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# 列表生成式
L = [x * x for x in range(1, 10)]
print(L)
# 将[] 换成 () 列表生成器
g = (x * x for x in range(1, 10))
print(g)

# 创建L和g的区别仅在于最外层的[]和()，L是一个list，而g是一个generator

# 如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值
g = (x * x for x in range(1, 10))
for n in g:
    print(n)

# 比如，著名的斐波拉契数列（Fibonacci），除第一个和第二个数外，任意一个数都可由前两个数相加得到：
# 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

print("斐波那契数列")


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return "done"


print(fib(10))

#  a, b = b, a + b 相当于
# t = (b, a + b) # t是一个tuple
# b = t[1]
# a = t[0]

# 上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：

print("斐波拉契数列生成器")


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return "done"


f = fib(10)
print(f)


# 举个栗子，依次返回数字1,3,5
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


for i in odd():
    print(i)

# 回到上面那个例子中，利用循环产生返回斐波拉契数列
for n in fib(10):
    print(n)

# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：

g = fib(10)
while True:
    try:
        x = next(g)
        print("g:", x)
    except StopIteration as e:
        print("Generator return value : ", e.value)
        break


# 输出杨辉三角形
# 杨辉三角定义如下：
#
#           1
#          / \
#         1   1
#        / \ / \
#       1   2   1
#      / \ / \ / \
#     1   3   3   1
#    / \ / \ / \ / \
#   1   4   6   4   1
#  / \ / \ / \ / \ / \
# 1   5   10  10  5   1
# 把每一行看做一个list，试写一个generator，不断输出下一行的list：

def triangles():
    lst = [1]
    count = 0
    while count < 10:
        yield lst
        lst = [1] + [(lst[i - 1] + lst[i]) for i in range(1, len(lst))] + [1]
        count += 1


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
