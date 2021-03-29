# def merge(li, low, mid, high):
#     i = low
#     j = mid + 1
#     ltemp = []
#     while i <= mid and j <= high:
#         if li[i] < li[j]:
#             ltemp.append(li[i])
#             i +=1
#
#         else:
#             ltemp.append(li[j])
#             j += 1
#     while i <= mid:
#         ltemp.append(li[i])
#         i +=1
#     while j <= high:
#         ltemp.append(li[j])
#         j +=1
#     # print(ltemp)
#     li[low: high+1] = ltemp
#
#
# def merge_sort(li, low, high):
#     if low < high:
#         mid = (low + high)//2
#         merge_sort(li, low, mid)
#         merge_sort(li, mid+1, high)
#
#         # ret = input('*****')
#         # print(low, mid, high, li[low:high + 1])
#         merge(li, low, mid, high)
#         # print(low, mid, high, li[low:high + 1])
#
#
lis = [10,4,6,3,8,2,5,7]
#
# import random
#
#
# merge_sort(li, 0, len(li)-1)
# print(li)


def one_merge(lis, start, mid, end):
    i = start
    j = mid+1
    templis = []
    while i <= mid and j <= end:
        if lis[i] < lis[j]:
            templis.append(lis[i])
            i += 1
        else:
            templis.append(lis[j])
            j += 1
    while i <= mid:
        templis.append(lis[i])
        i += 1
    while j <= end:
        templis.append(lis[j])
        j += 1
    lis[start:end+1] = templis


def gb_merge(lis, start, end):
    if start < end:
        mid = (start + end)//2
        gb_merge(lis, start, mid)
        gb_merge(lis, mid+1, end)
        one_merge(lis, start, mid, end)
