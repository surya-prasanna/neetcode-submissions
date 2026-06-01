class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        runningTotal = 0
        max_num = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                runningTotal += 1
            else:
                max_num = max(max_num, runningTotal)
                runningTotal = 0
        return max(max_num, runningTotal)
            
        