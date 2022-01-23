
import os
import random
from random import choice

ops = ('＋','－','×','÷')
ans = []
i=0
while i < 100 :
    op1 = choice(ops)
    op2 = choice(ops)
    n = random.randint(1,9)
    if op1 == '＋' and op2 == '＋' :
        a = random.randint(0,100)
        b = random.randint(0,100-a)
        c = random.randint(0,100-a-b)
        ans.append(a + b + c)
    elif op1 == '＋' and op2 == '－' :
        a = random.randint(0,100)
        b = random.randint(0,100-a)
        c = random.randint(0,a+b)
        ans.append(a + b - c)
    elif op1 == '＋' and op2 == '×' :
        b = random.randint(0,9)
        c = random.randint(0,9)
        a = random.randint(0, 100 - b * c)
        ans.append(a + b * c)
    elif op1 == '＋' and op2 == '÷':
        c = random.randint(1, 9)
        b = n * c
        a = random.randint(0, 100 - b / c)
        ans.append(a + b / c)
    elif op1 == '－' and op2 == '＋' :
        a = random.randint(0,100)
        b = random.randint(0,a)
        c = random.randint(0,100-a+b)
        ans.append(a - b + c)
    elif op1 == '－' and op2 == '－' :
        a = random.randint(0,100)
        b = random.randint(0,a)
        c = random.randint(0,a-b)
        ans.append(a - b - c)
    elif op1 == '－' and op2 == '×' :
        b = random.randint(0,9)
        c = random.randint(0,9)
        a = random.randint(b*c,100)
        ans.append(a - b * c)
    elif op1 == '－' and op2 == '÷':
        c = random.randint(1, 9)
        b = n * c
        a = random.randint(100 - b / c,100)
        ans.append(a - b / c)
    elif op1 == '×' and op2 == '＋' :
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0,100-a*b)
        ans.append(a * b + c)
    elif op1 == '×' and op2 == '－' :
        a = random.randint(0,9)
        b = random.randint(0,9)
        c = random.randint(0,a*b)
        ans.append(a * b - c)
    elif op1 == '÷' and op2 == '＋' :
        b = random.randint(1, 9)
        a = n * b
        c = random.randint(0,100 - a / b)
        ans.append(a / b + c)
    elif op1 == '÷' and op2 == '－' :
        b = random.randint(1,9)
        a = n * b
        c = random.randint(0,a / b)
        ans.append(a / b - c)
    else :
        continue
    print("第 %s 题： %s%s%s%s%s=" % (i + 1, a, op1, b, op2, c))
    i += 1
print("*"*60)
os.system("pause")


i = 0
while i < len(ans):
    print("第 %s 题答案：%d"%(i+1,ans[i]))
    i += 1
os.system("pause")

