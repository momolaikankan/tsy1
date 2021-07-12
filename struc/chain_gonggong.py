class Node():
    def __init__(self, item):
        self.item = item
        self.next = None
lis1 = [Node(1),Node(2),Node(5)]

lis2 = [Node(0),Node(2),Node(3),Node(4),Node(5)]

for j in range(len(lis1)-1):
    lis1[j].next = lis1[j+1]

for j in range(len(lis2)-1):
    lis2[j].next = lis2[j+1]

head1 = lis1[0]
head2 = lis2[0]
def func1(head1,head2):
    lis = []
    cur = head1
    while cur != None:
        lis.append(cur.item)
        cur = cur.next
    print(lis)
    cur1 = head2
    while cur1 !=None:
        if cur1.item in lis:
            print(cur1.item)
        cur1 = cur1.next
func1(head1,head2)

def func2(head1,head2):
    p1= head1
    p2 = head2
    while p1!=None and p2!= None:
        if p1.item == p2.item:
            print(p1.item)
            p1 = p1.next
            p2 = p2.next

        elif p1.item < p2.item:
            p1 = p1.next
        else:
            p2 = p2.next
func2(head1,head2)