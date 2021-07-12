def process(str1, index):
    if index == len(str1):
        return 1
    if str1[index] == '0':
        return 0
    if str1[index] == '1':
        res = process(str1, index+1)
        if index + 1 < len(str1):
            res += process(str1, index+2)
        return res
    if str1[index] == '2':
        res = process(str1, index + 1)
        if index+1 < len(str1) and (0 <= int(str1[index+1]) <= 6):
            res += process(str1, index+2)
        return res
    return process(str1, index+1)

res = process('110', 0)
print(res)


def func(str1, index):
    if index == len(str1):
        return 1
    if str1[index] == '0':
        return 0
    if str1[index] == '1':
        res = func(str1, index+1)
        if index +1 < len(str1):
            res += func(str1, index+2)
        return res
    if str1[index] == '2':
        res = func(str1, index+1)
        if index+1 < len(str1) and (0<= int(str1[index+1])<=6):
            res += func(str1, index+2)
        return res
    return func(str1, index+1)


def func1(str1, index):
    if index == len(str1):
        return 1
    res = func(str1,index+1)
    if index + 1 < len(str1):
        res += func(str1,index+2)
    return res


rk = func1('ab', 0)
print(rk)


def func2(str1, index):
    if index == len(str1):
        return 1
    if str1[index] == '0':
        return 0
    if str1[index] == '1':
        res = func2(str1, index+1)
        if index +1 < len(str1):
            res += func2(str1, index+2)
        return res
    if str1[index] == '2':
        res = func2(str1, index+1)
        if index +1 <len(str1) and (0 <= str1[index+1] <= 6):
            res += func2(str1, index+2)
        return res
    return func2(str1, index+1)
























