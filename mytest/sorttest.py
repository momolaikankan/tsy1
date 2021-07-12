lis = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
def gui(lis,left,right):
    if left == right:
        return
    mid = (left+right)//2
    gui(lis,left,mid)
    gui(lis,mid+1,right)
    p1 = left
    mid = (left+right)//2
    p2 = mid+1
    lis1 = []
    while p1 <= mid and p2 <= right:
        if lis[p1] < lis[p2]:
            lis1.append(lis[p1])
            p1 +=1
        elif lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            p2+=1
        else:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1+=1
            p2+=1
    while p1 <= mid:
        lis1.append(lis[p1])
        p1+=1
    while p2 <= right:
        lis1.append(lis[p2])
        p2+=1
    lis[left:right+1] = lis1
    return lis


res1 = gui(lis,0,len(lis)-1)
print(res1)

lis1 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
def kuai(lis1,left,right):
    if left > right:
        return
    l = left
    r = right
    temp = lis1[l]
    while l < r:
        while l < r:
            if lis1[r] > temp:
                r -=1
            else:
                lis1[l],lis1[r] = lis1[r],lis1[l]####
                break
        while l < r:
            if lis1[l] <= temp:
                l +=1
            else:
                lis1[l],lis1[r] = lis1[r],lis1[l]
                break
    lis1[l] = temp
    kuai(lis1,left,l-1)
    kuai(lis1,l+1,right)
    return lis1

res2 = kuai(lis1,0,len(lis1)-1)
print(res2)

lis2 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
def sift(lis,low,high):
    i = low
    j = 2*i+1
    temp = lis[low]
    while j <= high:
        if j+1 <=high and lis[j+1] < lis[j]:
            j = j+1
        if lis[j] < temp:
            lis[i] = lis[j]
            i = j
            j = 2*i+1
        else:
            lis[i] = temp
            break           ###
    else:
        lis[i] = temp
lis3 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]


def duisort(lis):
    n = len(lis)
    for i in range((n-2)//2, -1,-1):
        sift(lis,i,n-1)
    for i in range(n-1, -1,-1):
        lis[i],lis[0] = lis[0],lis[i]
        sift(lis,0,i-1)
    return lis

res3 = duisort(lis3)
print(res3)


def topk(lis,k):
    heap = lis[0:k]
    for i in range((k-2)//2, -1,-1):
        sift(heap,i,k-1)
    for i in range(k,len(lis)):
        if lis[i] > heap[0]:
            heap[0] = lis[i]
            sift(heap,0,k-1)
    for i in range(k-1,-1,-1):
        heap[0],heap[i] = heap[i],heap[0]
        sift(heap,0,i-1)
    return heap

res4 = topk(lis3,6)
print(res4)
