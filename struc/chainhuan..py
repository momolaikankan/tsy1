class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


lis = []
for i in range(1,10):
    node = Node(i)
    lis.append(node)



for j in range(len(lis)-1):
    lis[j].next = lis[j+1]
lis[-1].next = lis[4]

# cur = lis[0]
# while cur != None:
#     print(cur.item)
#     cur = cur.next

def kuaiman(node):
    p1 = node.next
    p2 = node.next.next
    while p1 != p2:
        p1 = p1.next
        p2 = p2.next.next
    p3 = node
    while p1 !=p3:
        p1 = p1.next
        p3 = p3.next
    print(p1.item)
    print(p3.item)
cur1 = lis[0]
kuaiman(cur1)