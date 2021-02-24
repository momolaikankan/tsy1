'''
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
'''
class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
class MyAdd():
    def __init__(self):
        self.head = None
    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def travel(self):
        cur = self.head
        while cur:
            print(cur.item, end='')
            cur = cur.next

    def myadd(self, node1, node2):
        node = Node(None)
        cur_index = node
        nd1 = node1
        nd2 = node2
        while nd1 and nd2:
            sum = nd1.item + nd2.item
            if sum >=10:
                shang, yu =divmod(sum, 10)
                nd1.next.item +=shang
                cur_node = Node(yu)
            else:
                cur_node = Node(sum)
            cur_index.next = cur_node
            cur_index = cur_index.next
            nd1 = nd1.next
            nd2 = nd2.next
        while nd1 or nd2:
            if nd1:
                cur_node = Node(nd1.item)
                cur_index.next = cur_node
                cur_index = cur_index.next
                nd1 = nd1.next
            if nd2:
                cur_node = Node(nd2.item)
                cur_index.next = cur_node
                cur_index = cur_index.next
                nd2 = nd2.next
        self.head = node.next
        return self.head


a = MyAdd()
a.add(3)
a.add(4)
a.add(2)
a.add(1)
a.travel()
b = MyAdd()
b.add(4)
b.add(6)
b.add(5)
b.travel()
c = MyAdd()
c.myadd(a.head,b.head)
c.travel()
for i in range(10):
    print(i)