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

# def hasCycle(head):
#     fast = slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             return True
#     return False
#
# print(hasCycle(l1_1))
#
# def detectCycle(head):
#     fast = slow = head
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if slow == fast:
#             break
#     slow = head
#     while slow != fast:
#         slow = slow.next
#         fast = fast.next
#     return slow.val
# print(detectCycle(l1_1))
#
# def findBinary(head):
#     slow = fast = head
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next
#     return slow.val
# print(findBinary(l1_1))
#
# def lastK(head,k):
#     slow = fast = head
#     while k > 0:
#         fast = fast.next
#         k -= 1
#     while fast.next:
#         slow = slow.next
#         fast = fast.next
#     return slow.val
# print(lastK(l1_1,2))

def binarySearch(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = int(left+(right-left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
nums = [1,3,5,6,7]
target = 6
print(binarySearch(nums,target))

def twoSum(nums,target):
    left = 0
    right = len(nums)-1
    while left <= right:
        sum = nums[left] + nums[right]
        if sum == target:
            return left+1,right+1
        elif sum > target:
            right -= 1
        elif sum < target:
            left += 1
    return -1,-1
nums = [1,3,5,6,7]
target = 7
print(twoSum(nums,target))

def reverse(nums):
    left = 0
    right = len(nums)-1
    while left <= right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums
nums = [1,3,5,6,7]
print(reverse(nums))

