def binarySearch(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left+(right-left)/2)
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    return -1
nums = [1,6,6,6,8]
target = 6
print(binarySearch(nums,target))

def binarySearch_L(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left+(right-left)/2)
        if nums[mid] == target:
            right = mid -1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    if left >= len(nums) or nums[left] != target:
        return -1
    return left
nums = [1,6,6,6,8]
target = 6
print(binarySearch_L(nums,target))

def binarySearch_R(nums,target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = int(left+(right-left)/2)
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
    if right >= len(nums) or nums[right] != target:
        return -1
    return right
nums = [1,6,6,6,8]
target = 6
print(binarySearch_R(nums,target))
