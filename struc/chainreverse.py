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



def singlereverse(node):
    if node.next == None:
        return node
    new_head = singlereverse(node.next)
    node.next.next = node
    node.next = None
    return new_head
#
# cur = lis[0]
# res = singlereverse(cur)
# while res != None:
#     print(res.item)
#     res = res.next
print('*****')
def myreverse(node):
    n1 = node
    n2 = node.next
    n1.next = None
    while n2 != None:
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    return n1
cur1 = lis[0]

res1 = myreverse(cur1)


while res1 != None:
    print(res1.item)
    res1 = res1.next


def rev(node):
    n1 = node
    n2 = node.next
    n1.next = None
    while n2!=None:
        n3 = n2.next
        n2.next = n1
        n1 = n2
        n2 = n3
    return n1

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