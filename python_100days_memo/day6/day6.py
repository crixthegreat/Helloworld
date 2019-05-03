"""在参数名前面的

* 表示 args 是一个可变参数

"""
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
	total = 0
	for val in args:
		total += val
	return total


print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))


from random import randint

def roll_dice(n=2):
	total = 0
	for _ in range(n):

        """ use the '_' to define a 
        
        __MEANINGLESS__ varible name
        
        """
            total += randint(1, 6)
	return total


def add(a=0, b=0, c=0):
	return a + b + c
