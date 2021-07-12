class Node():
    def __init__(self, item):
        self.item = item
        self.next = None


class Chain():
    def __init__(self):
        self.head = None

    def head_add(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def end_add(self, item):
        node = Node(item)
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def travel(self):
        cur = self.head
        while cur:
            print(cur.item)
            cur = cur.next







chain = Chain()
for i in range(5):
    chain.end_add(i)



chain.travel()


def myreverse(node):
    pre = node
    cur = node.next
    next_node = cur.next
    pre.next = None
    while next_node:
        cur.next = pre
        pre = cur
        cur = next_node
        next_node = next_node.next
    cur.next = pre
    return cur


def reverse2(head):
  if head.next == None: # 递归停止的基线条件
    return head
  new_head = reverse2(head.next)
  head.next.next = head # 当前层函数的head节点的后续节点指向当前head节点
  head.next = None # 当前head节点指向None
  return new_head


def myreverse2(node):
    if node.next == None:
        return node
    new_start = myreverse2(node.next)
    node.next.next = node
    node.next = None
    return new_start


res = myreverse2(chain.head)

while res:
    print(res.item)
    res = res.next























