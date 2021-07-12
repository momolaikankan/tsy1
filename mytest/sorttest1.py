lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
def kuai(lis,left,right):
    if left > right:
        return
    p1 = left
    p2 = right
    temp = lis[left]
    while p1 < p2:
        while p1 < p2:
            if lis[p2] > temp:
                p2 -= 1
            else:
                lis[p1], lis[p2] = lis[p2],lis[p1]
                break
        while p1 < p2:
            if lis[p1] <= temp:
                p1 +=1
            else:
                lis[p1], lis[p2] = lis[p2],lis[p1]
                break
    lis[p1] = temp
    kuai(lis,left,p1-1)
    kuai(lis,p1+1,right)
    return lis
res1 = kuai(lis,0,len(lis)-1)
print(res1)


def gui(lis,left,right):
    if left == right:
        return
    mid = (left+right)//2
    gui(lis,left,mid)
    gui(lis,mid+1,right)
    mid = (left+right)//2
    p1 = left
    p2 = mid+1
    lis1 = []
    while p1 <=mid and p2 <=right:
        if lis[p1]<lis[p2]:
            lis1.append(lis[p1])
            p1+=1
        elif lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            p2+=1
        else:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1+=1
            p2+=1
    while p1<=mid:
        lis1.append(lis[p1])
        p1+=1
    while p2 <=right:
        lis1.append(lis[p2])
        p2+=1
    lis[left:right+1] = lis1
    return lis1
lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
res2 = kuai(lis,0,len(lis)-1)
print(res2)

def sift(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1<=high and lis[j+1] > lis[j]:
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


def dui(lis):
    n = len(lis)
    for i in range((n-2)//2,-1,-1):
        sift(lis,i,n-1)
    for i in range(n-1,-1,-1):
        lis[i],lis[0] = lis[0],lis[i]
        sift(lis,0,i-1)
    return lis

lis = [3, 2, 1, 5, 4, 2, 3, 4, 5, 1, 16, 6, 7, 8, 9]
res3 = dui(lis)
print(res3)

def smallk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] < heap[0]:
            heap[0],lis[i] = lis[i],heap[0]
            sift(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)
    return heap
lis = [3, 2, 1, 5, 4, 2, 3, 4, 5, 1, 16, 6, 7, 8, 9]
res4 = smallk(lis,5)
print(res4)


def siftxiao(lis,low,high):
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
            break
    lis[i] = temp


def topk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        siftxiao(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] > heap[0]:
            heap[0],lis[i] = lis[i],heap[0]
            siftxiao(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        siftxiao(heap,0,i-1)
    return heap


lis = [3, 2, 1, 5, 4, 2, 3, 4, 5, 1, 16, 6, 7, 8, 9]
res5 = topk(lis,5)
print(res5)