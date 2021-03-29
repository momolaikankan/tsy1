def func(str1):
    lis = []
    for i in str1:
        lis.append(i)
    if len(lis) == 1:
        return '长度为1'
    while len(lis) >= 2:
        if lis.pop(0) == lis.pop():
            continue
        else:
            return 'no'
    else:
        return 'yes'
res = func('abcc')
print(res)

def func1(s):
    if len(s) < 2 or s == s[::-1]:
        return s
    n = len(s)
    # 定义起始索引和最大回文串长度，odd奇，even偶
    start, maxlen = 0, 1
    # 因为i=0的话必然是不可能会有超过maxlen情况出现，所以直接从1开始
    for i in range(1, n):
        # 取i及i前面的maxlen+2个字符
        odd = s[i - maxlen - 1:i + 1]  # len(odd)=maxlen+2
        # 取i及i前面的maxlen+1个字符
        even = s[i - maxlen:i + 1]  # len(even)=maxlen+1
        if i - maxlen - 1 >= 0 and odd == odd[::-1]:
            start = i - maxlen - 1
            maxlen += 2
            continue
        if i - maxlen >= 0 and even == even[::-1]:
            start = i - maxlen
            maxlen += 1
    return s[start:start + maxlen]


def func_get(s):
    hlen = 0
    strmax = ''
    for i in range(len(s)):
        len1 = len(ex_func(s, i, i))
        if len1 > hlen:
            hlen = len1
            strmax = ex_func(s, i, i)
        len2 = len(ex_func(s, i, i+1))
        if len2 > hlen:
            hlen = len2
            strmax = ex_func(s, i, i+1)
    return strmax


def ex_func(s, l, r):
    while l >= 0 and r < len(s):
        if s[l] == s[r]:
            l -= 1
            r += 1
            continue
        else:
            break
    return s[l+1: r]

print(func_get('aa'))