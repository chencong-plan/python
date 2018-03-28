# python当中对list 和tuple进行切片取元素

L = list(range(100))

print("前10个元素：", L[:10])

print("从第二个开始copy至末尾：", L[1:])

print("后10个元素：", L[-10:])

print("前11-20的元素:", L[10:20])

print("前10个元素，每隔2个取一个：", L[:10:2])

print("每5个取一个元素：", L[::5])

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()
str = "  chencong  "
print(str.strip())


# 定义一个函数
def trim(s):
    while s[:1] == " ":
        s = s[1:]
    while len(s) != 0 and s[-1] == " ":
        s = s[:-1]
    return s


# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
