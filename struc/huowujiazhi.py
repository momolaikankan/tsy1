def func(str1, lis, path, index):
    if index == len(str1):
        lis.append(path)
        return
    yes = path+str1[index]
    func(str1, lis, yes, index+1)
    no = path
    func(str1, lis, no, index+1)
    return lis


res = func('abc', [], '', 0)
print(res)


def func_value1(w,v,index,alreadyw,bag):
    if alreadyw > bag:
        return -1
    if index == len(w):
        return 0
    p1 = func_value1(w,v,index+1,alreadyw,bag)
    p2next = func_value1(w,v,index+1,alreadyw+w[index], bag)
    p2= -1
    if p2next != -1:
        p2 = p2next + v[index]
    return max(p1,p2)


def func_value(w, v, path, alreadyw, index, bag):
    if alreadyw > bag:
        return -1
    if index == len(w):
        return path
    no = path
    p2 = func_value(w, v, no, alreadyw, index+1, bag)
    yes = path+v[index]
    alreadyw += w[index]
    p1 = func_value(w, v, yes, alreadyw, index+1, bag)

    return max(p1, p2)


def func_value2(w,v,index,rest):
    if rest < 0:
        return -1
    if index == len(w):
        return 0
    p1 = func_value2(w,v,index+1,rest)
    p2 = -1
    p2next = func_value2(w,v,index+1,rest-w[index])
    if p2next != -1:
        p2 = p2next +v[index]
    return max(p1,p2)


def func_value_dp(w,v,index,rest,dp):

    if dp[rest][index] != -1:
        print(dp[rest][index])
        return dp[rest][index]
    if rest < 0:
        dp[rest][index] = -1
        return dp[rest][index]
    if index == len(w):
        dp[rest][index] = 0
        return dp[rest][index]
    p1 = func_value2(w,v,index+1,rest)
    p2 = -1
    p2next = func_value2(w,v,index+1,rest-w[index])
    if p2next != -1:
        p2 = p2next +v[index]
    return max(p1,p2)


def func_value_self_dp(w, v, path, alreadyw, index, bag, dp):
    if dp[alreadyw][index] != -1:
        print(dp[alreadyw][index])
        return dp[alreadyw][index]

    if alreadyw > bag:
        dp[alreadyw][index] = -1
        return dp[alreadyw][index]
    if index == len(w):
        dp[alreadyw][index] = path
        return dp[alreadyw][index]
    no = path
    p2 = func_value(w, v, no, alreadyw, index+1, bag)
    dp[alreadyw][index+1] = p2
    yes = path+v[index]
    alreadyw += w[index]
    p1 = func_value(w, v, yes, alreadyw, index+1, bag)
    dp[alreadyw][index+1] = p1

    return max(p1, p2)


def mydp(w, v, path, alreadyw, index, bag):
    dp = [[-1 for j in range(len(w)+1)] for i in range(20)]
    # return func_value_dp(w,v,index,rest,dp)
    return func_value_self_dp(w, v, path, alreadyw, index, bag, dp)


# w = [2,4,5,3]
# v = [5,4,6,2]
w = [2,2,6,5,4]

v = [6,3,5,4,6]
l =[3.0, 1.5, 0.8333333333333334, 0.8, 1.5]
bag = 10


res2= func_value1(w,v,0,0,bag)
print(res2)


res3= func_value2(w,v,0,bag)
print(res3)


res = func_value(w,v,0,0,0,bag)
print(res)


res4 = mydp(w,v,0,0,0,bag)
print('--',res4)

