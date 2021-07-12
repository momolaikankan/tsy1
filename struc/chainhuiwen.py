class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


lis = []
for i in range(1,4):
    node = Node(i)
    lis.append(node)
for i in range(3,0,-1):
    node = Node(i)
    lis.append(node)


for j in range(len(lis)-1):
    lis[j].next = lis[j+1]


cur = lis[0]
while cur != None:
    print(cur.item)
    cur = cur.next


def panduanhuiwen(node):
    lis1 = []
    cur = node
    while cur != None:
        lis1.append(cur)
        cur = cur.next
    cur1 = node
    for i in range(len(lis1)-1,-1,-1):
        if lis1[i].item == cur1.item:
            cur1 = cur1.next
            continue
        else:
            return False
    return True
node = lis[0]
res = panduanhuiwen(node)
print(res)


def kuaiman(node):
    p1 = node
    p2 = node.next
    while p2.next != None and p2.next.next !=None:
        p1 = p1.next
        p2 = p2.next.next
    print(p1.item)
    print(p1.next.item)
    print(p2.item)
kuaiman(lis[0])





