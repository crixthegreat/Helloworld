# the note index

## days 6 

- *args as function parameter (list)
- use the '_' for the meanlingless varible name 

## days 7

- use `yield` to make a generator
- refer to [Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)  by __廖 雪峰__ 

- Tuples is used to store values that are not intented to change
- use list() to change a tuple into a list
- a tuple with one item is constructed by following a value with a comma 

```
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(singleton)
1
>>> singleton
('hello',)
```

- use set() to make a set(collection)
- the operator of set are '&', '|', '-', '^', '<=', ... and so on


## day 9

### (1) A class has three types of method

1. instance method
2. static method
3. class method

refer to [day9-1.py](./day9/day9-1.py)

1. instance method

	the method can be used by the instance(object)
	use 'self' as the first argument 

2. static method

	the method can be used by the class and the instance
	use @staticmethod as the decorator

3. class method

	the class method can return a class itself
	which is useful to creat a specific instance(object)
	use @classmethod as the decorator

### (2) super().__init__(arg1, agr2, ...)

- use super() to return the parent class
- super can be used to refer to parent classes without naming them explicitly, thus making the code more maintainable
- refer to artical: [Python's super() considered super!](https://rhettinger.wordpress.com/2011/05/26/super-considered-super/) by __Raymond Hettinger__


## day10

a brief introduction of tkinker and pygame


## day11

a brief introduction of exception
refer to [总结：Python中的异常处理](./day11/refer/总结：Python中的异常处理.md) by __betacat__
