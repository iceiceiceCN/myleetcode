nums = [1,2,2,4]
val = 2
def removeElement(nums, val):
    while val in nums:
        nums.pop(nums.index(val))

removeElement(nums,val)