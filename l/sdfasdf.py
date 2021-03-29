import os
lock_dir = r'D:\\projects\\JYW\\asset\\char\\bieYangHong_CA0008_Char_RG\\Tpose\\yuxuan'
# os.makedirs(lock_dir)
lis = [4,3,1,2,6,9,8,7]
def mysort(lis, start, end):
    low = start
    high = end
    if low > high:
        return
    temp = lis[start]
    while low < high:
        while low < high:
            if temp < lis[high]:
                high -= 1
            else:
                lis[low] = lis[high]
                break
        while low < high:
            if temp > lis[low]:
                low += 1
            else:
                lis[high] = lis[low]
                break
        if low == high:
            lis[low] = temp
            break
    mysort(lis, start, low-1)
    mysort(lis, low+1, end)
    return lis


def qsort(lis, start, end):
    mid = lis[start]
    while start < end:
        while start < end and lis[end] > mid:
            end -= 1
        lis[start] = lis[end]
        while start < end and lis[start] < mid:
            start += 1
        lis[end] = lis[start]
    lis[start] = mid
    return start


def qq_sort(lis, start, end):
    if start < end:
        mid = qsort(lis, start, end)
        qq_sort(lis, start, mid-1)
        qq_sort(lis, mid+1, end)


ret = mysort(lis, 0, len(lis)-1)
print(ret)

print(qq_sort(lis, 0, len(lis)-1))


