class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
lis = []
for i in range(5):
    node = Node(i)
    lis.append(node)

for j in range(len(lis)-1):
    lis[j].next = lis[j+1]

cur = lis[0]
while cur != None:
    print(cur.item)
    cur = cur.next


def chainreverse(node):
    if node.next == None:
        return node
    new_head = chainreverse(node.next)
    node.next.next = node
    node.next = None
    return new_head


cur = chainreverse(lis[0])

while cur != None:
    print(cur.item)
    cur = cur.next
