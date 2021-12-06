def binarySearch(nums, min, max, elem):
    mid = (max + min) // 2
    if(min > max):
        print("Element is not present in array")
    elif(elem < nums[mid]):
        binarySearch(nums, min, mid, elem)
    elif(elem > nums[mid]):
        binarySearch(nums, mid+1, max, elem)
    else:
        print(f"Element is present at index {min}")


n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

nums.sort()

print("Initially array is:", nums)
elem = int(input("element to be searched:"))
print(elem)
binarySearch(nums, 0, len(nums)-1, elem)
