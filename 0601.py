class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(4)
l1_4 = ListNode(6)
l1_5 = ListNode(8)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = None

def reverseListLR(a,b):
    current = a
    next = a
    pre = None
    while current != b:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre
#print(reverseListLR(l1_1,l1_4))

def reverseKGroup(head,K):
    if head == None:
        return None
    a = b = head
    for i in range(K):
        if b == None:
            return head
        b = b.next

    newHead = reverseListLR(a,b)
    a.next = reverseKGroup(b,K)
    return newHead
k = 2
print(reverseKGroup(l1_1,k))