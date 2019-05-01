# coding:utf-8
import os
import random
os.system('cls')

print("现在开始练习啦！")

Times = int(input("请问你想做几道题？ "))
while Times > 20 or Times < 3:
    if Times>20:
        print("你一次做太多啦！不要超过20道！")
        print()
    elif Times<3:
        print("你一次做太少啦！不要少于3道！")
        print()
    Times = int(input("请问你想做几道题？ "))

WinTimes = 0
for i in range(Times):
    print("第 {} 题:".format(i+1))
    print()
    a = random.randint(1,50)
    b = random.randint(1,50)
    calType = random.randint(1,2)
    if a < b:
        t = a
        a = b
        b = t
    if calType == 1:
        Result = int(input("{} + {} = ".format(a,b)))
        if Result == (a + b):
            WinTimes += 1
            print("你做对啦！真棒！，你已经做对了 {} 题".format(WinTimes))
            print()
        else:
            print("很遗憾你做错啦，要仔细一点哦！")
            print()
    else:
        Result = int(input("{} - {} = ".format(a,b)))
        if Result == (a - b):
            WinTimes += 1
            print("你做对啦！真棒！，你已经做对了 {} 题".format(WinTimes))
            print()
        else:
            print("很遗憾你做错啦，要仔细一点哦！")
            print()
print("全部题目都做完啦，你一共做了 {} 题，做对了 {} 题".format(Times, WinTimes))
if WinTimes == Times:
    print("你全部做对啦！真的很棒！请继续努力哦！")
else:
    print("你还有做错的题目，要继续加油啊！")

