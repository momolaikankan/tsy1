def sift(lis, low, high):
    i = low
    j = 2*i+1
    # if low > high:
    #     return
    temp = lis[low]
    while j <= high:
        if j+1 <= high and lis[j+1] > lis[j]:
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


def heap_sort(lis):
    n = len(lis)
    for i in range((n-2)//2, -1, -1):
        sift(lis, i, n-1)
    for i in range(n-1, -1, -1):
        lis[0], lis[i] = lis[i], lis[0]
        sift(lis,0,i-1)
    return lis


lis = [1,2,3,54,3,2,3,4,5,6,7,]

res =  heap_sort(lis)
print(res)



































def sift2(lis,low, high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1<=high and lis[j+1] < lis[j]:
            j = j+1
        if lis[j] < temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i] = temp
            break
    else:
        lis[i] = temp


def heapsort(lis):
    n = len(lis)
    for i in range((n-2)//2, -1, -1):
        sift2(lis, i, n-1)
    for i in range(n-1, -1, -1):
        lis[i], lis[0] = lis[0], lis[i]
        sift2(lis, 0, i-1)


lis = [1,2,3,54,3,2,3,4,5,6,7,]


heapsort(lis)
print(lis)


def topk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2, -1, -1):
        sift2(heap,i,k-1)
    for j in range(k,len(lis)):
        if lis[j] > heap[0]:
            heap[0] = lis[j]
            sift2(heap,0,k-1)
    for i in range(k-1, -1,-1):
        heap[0], heap[i] = heap[i],heap[0]
        sift2(heap,0,i-1)
    return heap

lis2 = [4,3,2,5,6,7,8,9,10,1]
print('************')
res  = topk(lis2,5)
print(res)


def sift3(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1 <= high and lis[j+1] < lis[j]:
            j = j+1
        if lis[j] < temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i] = temp
            break
    else:
        lis[i] = temp


def topk2(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        sift3(heap,0,k-1)
    for j in range(k,len(lis)):
        if lis[j] > heap[0]:
            heap[0] = lis[j]
            sift3(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[i],heap[0] = heap[0],heap[i]
        sift3(heap, 0, i-1)
    return heap
lis2 = [4,3,2,5,6,7,8,9,10,1]

res1 = topk2(lis2,5)
print(res1)





def sift4(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j +1 <=high and lis[j+1] < lis[j]:
            j = j+1
        if lis[j] < lis[i]:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i] = temp
            break
    else:
        lis[i] = temp



def duisort(lis):
    n = len(lis)
    for i in range((n-2)//2, -1, -1):
        sift4(lis,i,n-1)
    for i in range(n-1,-1,-1):
        lis[0],lis[i] = lis[i],lis[0]
        sift4(lis,0,i-1)
    return lis



def topk3(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        sift4(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] > heap[0]:
            heap[0] = lis[i]
            sift4(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[0], heap[i] = heap[i],heap[0]
        sift4(heap,0, i-1)
    return heap

lis3 = [4,3,2,5,6,7,8,9,10,1]
res4 = duisort(lis3)
print(res4)
res3 = topk3(lis3,5)
print(res3)











































