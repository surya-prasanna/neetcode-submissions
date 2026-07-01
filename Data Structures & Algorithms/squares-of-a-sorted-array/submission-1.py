class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        res_index = r = len(nums) - 1

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                res[res_index] = nums[l] * nums[l]
                l += 1
            else:
                res[res_index] = nums[r] * nums[r]
                r -= 1
            
            res_index -= 1
        return res
        