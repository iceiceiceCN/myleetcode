class Solution:
    def twoSum(self,numbers,target):
        leftIndex = 0
        rightIndex = len(numbers)-1
        while leftIndex < rightIndex:
            if numbers[leftIndex] + numbers[rightIndex] == target:
                return [leftIndex+1, rightIndex+1]
            elif numbers[leftIndex] + numbers[rightIndex] > target:
                rightIndex -= 1
            else:
                leftIndex += 1
        return [] 
        
# 看到有序数组就想到双指针！！