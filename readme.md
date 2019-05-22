# the note index

## days 6 

- `*args` as function parameter (list)
- use the `_` for the meanlingless varible name 

## days 7

- use `yield` to make a generator
- refer to [Python yield 使用浅析](https://www.ibm.com/developerworks/cn/opensource/os-cn-python-yield/)  by __廖 雪峰__ 

- Tuples is used to store values that are not intented to change
- use `list()` to change a tuple into a list
- a tuple with one item is constructed by following a value with a comma 

```
>>> singleton = 'hello',    # <-- note trailing comma
>>> len(singleton)
1
>>> singleton
('hello',)
```

- use `set()` to make a set(collection)
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

## day12

a brief introduction of `strings` and Regular Expression
refer to [正则表达式30分钟入门教程(by deerchao)](https://deerchao.net/tutorials/regex/regex.htm)

- useful strings methods:<br>
bool type : `str.isalpha()` (alpha-beta)  `str.isdecimal()`(numbers)  `str.isalnum`(alpha-beta and numbers)<br>
fuctions: `'-'.join(list)`  `sentence.split(',')` `pyperclip.copy('老虎不发猫你当我病危呀')`  `print(pyperclip.paste())`
- to trim a str:
```
t = t[:len(t) -1]  
# which equals to
t=t[::-1][1:][::-1]
```

- to use regulaer expression in python , 
```
import re
re.match()
re.sub
re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
```

## day13
Process and threads 进程和线程

- refer to [知乎：线程和进程的区别是什么？](https://www.zhihu.com/question/25532384)
- refer to [examples](https://github.com/crixthegreat/Python-100-Days/tree/master/Day01-15/Day13/code)

## day14 A/B

- listen and send message via sockets
- use threads to accept mutil-user events simultaneously
- send emails and text-messages

## day15
- PIL module to deal with images

## day16
advance programming of python

- generator and iterator
- multi-thread program

## day21
web front-end

## day31
a brief introduction of Linux

## day36
NoSQL & MySQL

## day41
a introduction of Danjo 
