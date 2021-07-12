
def func(lis, left, right):
    if left == right:
        return
    mid = (left+right)//2
    func(lis,left,mid)
    func(lis,mid+1,right)
    mymegrge(lis,left, mid, right)


def mymegrge(lis, left, mid, right):
    p1 = left
    p2 = mid+1
    lis1 = []
    while p1 <= mid and p2 <= right:
        if lis[p1] < lis[p2]:
            lis1.append(lis[p1])
            p1 += 1
            continue
        elif lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            p2 += 1
            continue
        elif lis[p1] == lis[p2]:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1 += 1
            p2 += 1
            continue
    while p1 <= mid:
        lis1.append(lis[p1])
        p1 += 1
    while p2 <= right:
        lis1.append(lis[p2])
        p2 += 1
    lis[left:right+1] = lis1


lis = [3,2,1,5,4,2,3]
func(lis,0,len(lis)-1)
print(lis)


def mymerge1(lis, left, mid, right):
    p1 = left
    p2 = mid+1
    lis1 = []
    while p1 <= mid and p2 <=right:
        if lis[p1] < lis[p2]:
            lis1.append(lis[p1])
            p1 += 1
            continue
        if lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            p2+=1
            continue
        if lis[p1] == lis[p2]:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1 +=1
            p2 +=1
            continue
    while p1 <= mid:
        lis1.append(lis[p1])
        p1+=1
    while p2 <= right:
        lis1.append(lis[p2])
        p2 += 1
    lis[left:right+1] = lis1


def func1(lis,left,right):
    if left == right:
        return
    mid = (left+right)//2
    func1(lis,left,mid)
    func1(lis,mid+1,right)
    mymerge1(lis,left,mid,right)
    return lis

lis1 = [3,2,1,5,4,2,3]
res1 = func1(lis1,0,len(lis1)-1)
print(res1)


def gui(lis,left,right):
    if left == right:
        return
    mid = (left+right)//2
    gui(lis,left,mid)
    gui(lis,mid+1,right)
    p1 = left
    p2 = mid+1
    lis1 = []
    while p1 <= mid and p2 <=right:
        if lis[p1] < lis[p2]:
            lis1.append(lis[p1])
            p1 += 1
            continue
        if lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            p2+=1
            continue
        if lis[p1] == lis[p2]:
            lis1.append(lis[p1])
            lis1.append(lis[p2])
            p1 +=1
            p2 +=1
            continue
    while p1 <= mid:
        lis1.append(lis[p1])
        p1+=1
    while p2 <= right:
        lis1.append(lis[p2])
        p2 += 1
    lis[left:right+1] = lis1
    return lis
lis2 = [3,2,1,5,4,2,3]
res2 = gui(lis2,0,len(lis2)-1)
print(res2)