class ListNode(object):
    def __init__(self,x):
        self.val = x
        self.next = None

l1_1 = ListNode(1)
l1_2 = ListNode(2)
l1_3 = ListNode(3)
l1_4 = ListNode(4)
l1_5 = ListNode(5)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4
l1_4.next = l1_5
l1_5.next = None

def reverseLR(a,b):
    current = next = a
    pre = None
    while current != b:
        next = current.next
        current.next = pre
        pre = current
        current = next
    return pre

def reverseKGroup(head1,head,k):
    if head == None:
        return None
    a = b = head
    for i in range(k):
        if b == None:
            return head
        b = b.next
    newHead = reverseLR(a,b)
    if head1 != None:
        for i in range(k):
            head1 = head1.next
        head1 = newHead
    a.next = reverseKGroup(newHead,b,k)
    return newHead
k = 2
print(reverseKGroup(None,l1_1,k))