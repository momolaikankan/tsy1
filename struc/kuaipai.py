lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]


def func(lis, start, end):

    left = start
    right = end
    if left > right:
        return
    temp = lis[start]
    while left < right:
        while left < right:
            if lis[right] >= temp:
                right -= 1
                continue
            elif lis[right] < temp:
                lis[left], lis[right] = lis[right], lis[left]
                break
        while left < right:
            if lis[left] <= temp:
                left += 1
                continue
            elif lis[left] > temp:
                lis[left], lis[right] = lis[right], lis[left]
                break
    lis[left] = temp
    func(lis, start, left-1)
    func(lis, left+1, end)
    return lis


res = func(lis,0,len(lis)-1)

print(res)









def mysort(lis,left,right):
    if left > right:
        return
    l = left
    r = right
    temp = lis[l]
    while l < r:
        while l < r:
            if lis[r] >temp:
                r -= 1
            else:
                lis[l],lis[r] = lis[r],lis[l]
                break
        while l < r:
            if lis[l] <= temp:
                l+= 1
            else:
                lis[l], lis[r] = lis[r], lis[l]
                break
    lis[l] = temp
    mysort(lis,left,r-1)
    mysort(lis,r+1,right)
    return lis
lis1 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]

res1 = mysort(lis1, 0, len(lis1)-1)
print(res1)






