class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


lis1 = [3,2,1,5,4,2,3,4,5,1,16,6,7,8,9]
lis = []
for i in lis1:
    node = Node(i)
    lis.append(node)

for j in range(len(lis)-1):
    lis[j].next = lis[j+1]

cur = lis[0]
while cur != None:
    print(cur.item)
    cur = cur.next

def chainpaixu(head, num):
    lis = []
    cur = head
    while cur!= None:
        lis.append(cur.item)
        cur = cur.next
    left = 0
    index = 0
    right = len(lis)-1
    while index !=right:
        if lis[index] < num:
            lis[index], lis[left] = lis[left],lis[index]
            index +=1
            left+=1
        elif lis[index] == num:
            index +=1
        else:
            lis[index],lis[right] = lis[right],lis[index]
            right -= 1
    print(lis)
    lis1 = []
    for i in range(len(lis)):
        lis1.append(Node(lis[i]))

    for j in range(len(lis1)-1):
        lis1[j].next = lis1[j+1]
    return lis1[0]


res = chainpaixu(lis[0],5)
print('*****')

while res!= None:
    print(res.item)
    res = res.next