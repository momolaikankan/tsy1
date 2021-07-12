lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
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
    while p1 <= mid and p2 <=right:
        if lis[p1] < lis[p2]:
            lis1.append(lis[p1])
            p1+=1
        elif lis[p1]>lis[p2]:
            lis1.append(lis[p2])
            p2+=1
        else:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1+=1
            p2+=1
    while p1<= mid:
        lis1.append(lis[p1])
        p1+=1
    while p2<=right:
        lis1.append(lis[p2])
        p2+=1
    lis[left:right+1] = lis1
    return lis

res1 = gui(lis, 0,len(lis)-1)
print(res1)

def kuai(lis,left,right):
    if left > right:
        return
    l = left
    r = right
    temp = lis[left]   ###
    while l < r:
        while l < r:
            if lis[r] > temp:
                r-=1
            else:
                lis[l],lis[r] = lis[r],lis[l]
                break
        while l < r:
            if lis[l] <= temp:
                l +=1
            else:
                lis[l],lis[r] = lis[r],lis[l]
                break
    lis[l] = temp
    kuai(lis, left, l-1)
    kuai(lis, l+1, right)
    return lis

lis1 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
res2 = kuai(lis1,0,len(lis1)-1)
print(res2)

def sift(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1 <= high and lis[j+1] > lis[j]:
            j= j+1
        if lis[j] > temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i]  = temp
            break
    else:
        lis[i] = temp


def bigdui(lis):
    n = len(lis)
    for i in range((n-2)//2,-1,-1):
        sift(lis,i,n-1)
    for i in range(n-1,-1,-1):
        lis[0],lis[i] = lis[i],lis[0]
        sift(lis,0,i-1)
    return lis

lis2 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
res2 = bigdui(lis2)
print(res2)


def siftxiao(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1 <= high and lis[j+1] < lis[j]:
            j= j+1
        if lis[j] < temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i]  = temp
            break
    else:
        lis[i] = temp

def topk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        siftxiao(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] > heap[0]:
            heap[0] = lis[i]
            siftxiao(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[i],heap[0] = heap[0],heap[i]
        siftxiao(heap,0, i-1)
    return heap
lis3 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
res3 = topk(lis3,6)
print(res3)


def smallk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2,-1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] < heap[0]:
            heap[0] = lis[i]
            sift(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[i],heap[0] = heap[0],heap[i]
        sift(heap,0, i-1)
    return heap
lis4 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
res4 = smallk(lis4,6)
print(res4)