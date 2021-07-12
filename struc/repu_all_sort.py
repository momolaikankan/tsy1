def permutation(S):
    n=len(S)
    if n==0:
        return [""]
    res=[]
    for i in range(n):
        if S[i] in S[:i]:   #只需判断S[i]是否在S[:i]中出现过即可
            continue
        for s1 in permutation(S[:i]+S[i+1:]):
            res.append(S[i]+s1)
    return res


def perm(arr):
    """实现全排列"""
    length = len(arr)
    if length == 1:  # 递归出口
        return [arr]

    result = []  # 存储结果
    fixed = arr[0]
    rest = arr[1:]

    for _arr in perm(rest):  # 遍历上层的每一个结果
        for i in range(0, length):  # 插入每一个位置得到新序列
            new_rest = _arr.copy()  # 需要复制一份
            new_rest.insert(i, fixed)
            result.append(new_rest)
    return result


res = permutation('abc')
# print(res)
# s = 'abc'
# print(s[:1]+s[2:])


def permutations(arr, position, end):
    if position == end:
        print(arr)
    else:
        for index in range(position, end):
            if arr[index] not in arr[index+1:]:
                arr[index], arr[position] = arr[position], arr[index]
                permutations(arr, position + 1, end)
                arr[index], arr[position] = arr[position], arr[index]


arr = 'abc'









print('*******************')











































def allsort(lis, pos, end):
    if pos == end:
        print(lis)
        return
    for index in range(pos, end):
        lis[index], lis[pos] =lis[pos], lis[index]
        allsort(lis, pos+1, end)
        lis[pos], lis[index] = lis[index], lis[pos]


lis = [1,2,1]

allsort(lis, 0, len(lis))