lis = [1,2,3,4,5]


def myreverse(lis):
    res = lis.pop(0)
    if len(lis) == 0:
        return [res]
    one = myreverse(lis)
    one.append(res)
    return one


res = myreverse(lis)

print(res)