lis = [2,3,4,5,6,5,7,8,5,3,9,8]

def func(lis, num):
    left = 0
    right = len(lis)-1
    index = 0
    while index < right:
        if lis[index] < num:
            lis[left], lis[index] = lis[index], lis[left]
            left += 1
            index += 1
        elif lis[index] > num:
            lis[right], lis[index] = lis[index], lis[right]
            right -= 1
        elif lis[index] == num:
            index += 1
    return lis

res = func(lis,5)
print(lis)





def func1(lis):
    left = 0
    right = len(lis)-1
    index = 0
    num = 5
    while index < right:
        if lis[index] < num:
            lis[index],lis[left] = lis[left],lis[index]
            index +=1
            left += 1
        elif lis[index] == num:
            index +=1
        else:
            lis[index],lis[right] = lis[right],lis[index]
            right -= 1
    return lis
res1 = func(lis,5)
print(res1)