lis = ['a', 'b', 'c']
def zisort(lis):
    res = lis.pop()
    if len(lis) == 0:
        return [[res],[]]
    kk = []
    new_lis = zisort(lis)
    for one_lis in new_lis:
        origin_lis = one_lis[:]
        origin_lis.append(res)
        kk.append(origin_lis)
        kk.append(one_lis)
    return kk
res = zisort(lis)
# print(res)


def zisort(str1, index, ans, path):
    if index == len(str1):
        ans.append(path)
        return
    yes = path + str1[index]
    zisort(str1, index + 1, ans, yes)
    no = path
    zisort(str1, index + 1, ans, no)
    return ans
res1 = zisort('abb', 0, [], '')
print(res1)


def duzisort(str1, index, ans, path):
    if index == len(str1):
        if path not in ans:
            ans.append(path)
        return
    yes = path + str1[index]
    duzisort(str1, index + 1, ans, yes)
    no = path
    duzisort(str1, index + 1, ans, no)
    return ans


res1 = duzisort('abb', 0, [], '')
print(res1)


def zisort2(str1, index, ans, path):
    if index == len(str1):
        ans.append(path)
        return
    yes = path + str1[index]
    zisort2(str1, index + 1, ans, yes)
    no = path
    zisort2(str1, index + 1, ans, no)
    return ans
res1 = zisort2('abb', 0, set(), '')
print(res1)