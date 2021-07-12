lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
def gui(lis,left,right):
    if left==right:
        return
    mid = (left+right)//2
    gui(lis,left,mid)
    gui(lis,mid+1,right)

    l = left


    r = mid+1
    lis1 = []
    while l <= mid and r <= right:
        if lis[l] < lis[r]:
            lis1.append(lis[l])
            l += 1
        elif lis[l] > lis[r]:
            lis1.append(lis[r])
            r+=1
        else:
            lis1.append(lis[l])
            lis1.append(lis[r])
            l +=1
            r+=1
    while l <= mid:
        lis1.append(lis[l])
        l+=1
    while r <=right:
        lis1.append(lis[r])
        r += 1
    lis[left:right+1] = lis1
    return lis

res = gui(lis,0,len(lis)-1)
print(res)


# def kuai(lis,left,right):
#     if left > right:
#         return
#     l = left
#     r = right
#     temp = lis[l]
#     while l < r:
#         while l < r:
#             if lis[r] >temp:####这里
#                 r -= 1
#             else:
#                 lis[l],lis[r] = lis[r],lis[l]
#                 break
#         while l < r:
#             if lis[l] <=temp:###这里
#                 l += 1
#             else:
#                 lis[l],lis[r] = lis[r],lis[l]
#                 break
#     lis[l] = temp
#     kuai(lis,left,l-1)
#     kuai(lis,l+1,right)
#     return lis
#
#
# res1 = kuai(lis,0,len(lis)-1)
# print(res1)


# def sift(lis,low,high):
#     i = low
#     j = 2*i+1
#     temp = lis[low]
#     while j <= high:
#         if j+1 <=high and lis[j+1]> lis[j]:
#             j = j+1
#         if lis[j] > temp:
#             lis[i] = lis[j]
#             i = j
#             j = 2*i+1
#         else:
#             lis[i] = temp
#             break
#     else:
#         lis[i] = temp
#
#
# def duisort(lis):
#     n = len(lis)
#     for i in range((n-2)//2,-1,-1):
#         sift(lis,i,n-1)
#     for i in range(n-1,-1,-1):
#         lis[0],lis[i] = lis[i],lis[0]
#         sift(lis,0,i-1)
#     return lis
#
# res2 = duisort(lis)
# print(res2)
#
# def siftxiao(lis,low,high):
#     i = low
#     j = 2*i+1
#     temp = lis[low]
#     while j <= high:
#         if j+1 <=high and lis[j+1]< lis[j]:
#             j = j+1
#         if lis[j] < temp:
#             lis[i] = lis[j]
#             i = j
#             j = 2*i+1
#         else:
#             lis[i] = temp
#             break
#     else:
#         lis[i] = temp
#
# def topk(lis,k):
#     heap = lis[0:k]
#     for i in range((k-2)//2,-1,-1):
#         siftxiao(heap,i,k-1)
#     for i in range(k,len(lis)):
#         if lis[i] > heap[0]:
#             heap[0] = lis[i]
#             siftxiao(heap,0,k-1)
#     for i in range(k-1,-1,-1):
#         heap[0],heap[i] = heap[i],heap[0]
#         siftxiao(heap,0,i-1)
#     return heap
# res3 = topk(lis,5)
# print(res3)