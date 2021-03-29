'''每一个堆通过一次向下调整方法，变成一个大根堆，-------依次出数，然后'''

# def sift(li, low, high):
#     i = low
#     j = 2*i+1
#     temp = li[low]
#     while j <= high:
#         if j + 1 <= high and li[j+1] > li[i]:
#             j = j+1
#         if li[j] > temp:
#             lis[i] = lis[j]
#             i = j
#             j = 2*i+1
#         else:
#             li[i] = temp
#             break
#     else:
#         li[i] = temp
#
#
# def heap_sort(li):
#     ##########建堆
#     n = len(li)
#     for i in range((n-2)//2, -1, -1):
#         sift(li, i, n-1)
#     for i in range(n-1, -1, -1):
#         sift(li, 0, i-1)

def sift(lis, low, high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if lis[j] < lis[j+1] and j+1 <= high:
            j = j+1
        if lis[j] > temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i] = temp
            break
    else:
        lis[i] = temp


def head_sort(lis):
    n = len(lis)
    for i in range((n-2)//2, -1, -1):
        sift(lis, i, n-1)
    for i in range(n-1, -1, -1):
        lis[0], lis[i] = lis[i], lis[0]
        sift(lis, 0, i-1)


lis = [6, 4, 3, 1, 2, 5, 7, 9, 8]
head_sort(lis)
print(lis)


