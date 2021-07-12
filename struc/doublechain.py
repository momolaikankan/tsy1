class Node():
    def __init__(self, item):
        self.item = item
        self.before = None
        self.next = None
lis = []
for i in range(5):
    node = Node(i)
    lis.append(node)

for j in range(len(lis)):
    if j ==0:
        lis[j].next = lis[j+1]
    elif j == len(lis)-1:
        lis[j].before = lis[j-1]
    else:
        lis[j].next = lis[j+1]
        lis[j].before = lis[j-1]



cur = lis[0]
while cur != None:
    print(cur.item)
    cur = cur.next
cur = lis[-1]
while cur !=None:
    print(cur.item)
    cur = cur.before


def doublereverse(node):
    if node.next == None:
        node.before = None
        return node
    new_node = doublereverse(node.next)
    node.next.next = node
    node_next = node.next
    node.next = node.before
    node.before = node_next
    return new_node
print('******')

# cur = doublereverse(lis[0])
# print(cur.item)
# while cur.next!= None:
#     print(cur.item)
#     cur = cur.next
# cur1 = cur
# while cur1!= None:
#     print(cur1.item)
#     cur1 = cur1.before

# cur = doublereverse(lis[0])
# while cur !=None:
#     print(cur.item)
#     cur = cur.before


# def doublereverse(node):
#     if node.next == None:
#         node.before = None
#         return node
#     new_head = doublereverse(node.next)
#     node.next.next = node
#     node_next = node.next
#     node.next = node.before
#     node.before = node_next
#     return new_head

print('________________')
def doublereverse1(node):
    n1 = node
    n2 = n1.next
    n1.next = None
    while n2!= None:
        n3 = n2.next
        n2.next = n1
        n1.before = n2
        n1 = n2
        n2 = n3
    n1.before = None
    return n1
cur = doublereverse1(lis[0])
print(cur.item)
while cur.next!= None:
    print(cur.item)
    cur = cur.next
cur1 = cur
while cur1!= None:
    print(cur1.item)
    cur1 = cur1.before