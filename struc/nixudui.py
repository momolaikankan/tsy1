def func(lis, left, right):
    if left == right:
        return
    mid = (left+right)//2
    func(lis,left,mid)
    func(lis,mid+1,right)
    mymerge(lis,left, mid, right)


def mymerge(lis, left, mid, right):
    p1 = left
    p2 = mid+1
    lis1 = []
    while p1 <= mid and p2 <= right:
        if lis[p1] <= lis[p2]:
            lis1.append(lis[p1])
            p1 += 1
            continue
        elif lis[p1] > lis[p2]:
            lis1.append(lis[p2])
            for i in range(p1,mid+1):
                print(lis[i],lis[p2])
            p2 += 1
            continue

    while p1 <= mid:
        lis1.append(lis[p1])
        p1 += 1
    while p2 <= right:
        lis1.append(lis[p2])
        p2 += 1
    lis[left:right+1] = lis1


lis = [3,2,1,5,4]
func(lis,0,len(lis)-1)
print(lis)


