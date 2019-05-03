"""the yield

when a function uses 'yield' statment,
it becomes a generator rather than a function
which means it WILL NOT RUN when it's called
it runs only when the next() method is called

in this example, the 'for' block calls the next() method automatically
"""


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
	for val in fib(20):
	    print(val)


if __name__ == '__main__':
	main()


def my_tuple():
	# 定义元组
	t = ('骆昊', 38, True, '四川成都')
	print(t)
	# 获取元组中的元素
	print(t[0])
	print(t[3])
	# 遍历元组中的值
	for member in t:
		print(member)
	# 重新给元组赋值
	# t[0] = '王大锤'  # TypeError
	# 变量t重新引用了新的元组原来的元组将被垃圾回收
	t = ('王大锤', 20, True, '云南昆明')
	print(t)
	# 将元组转换成列表
	person = list(t)
	print(person)
    # 列表是可以修改它的元素的
	person[0] = '李小龙'
	person[1] = 25
	print(person)
    # 将列表转换成元组
	fruits_list = ['apple', 'banana', 'orange']
	fruits_tuple = tuple(fruits_list)
	print(fruits_tuple)
