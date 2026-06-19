class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = ans = nums[0]
        

        for i in range(len(nums) - 1):
            if nums[i + 1] > nums[i]:
                res += nums[i + 1]
            else:
                ans = max(ans, res)
                res = nums[i + 1]

        return max(ans, res)
            
