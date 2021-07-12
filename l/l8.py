def huiwen(num):
    lis = []
    for i in str(num):
        lis.append(i)
    while len(lis) > 1:
        if lis.pop() != lis.pop(0):
            return False
    return True
res = huiwen(11)
print(res)



