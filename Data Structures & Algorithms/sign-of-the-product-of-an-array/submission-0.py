def signFunc(nums: List[int]) -> int:
    negatives = 0
    for num in nums: 
        if num < 0:
            negatives += 1
        elif num > 0:
            continue
        else:
            return 0
    if negatives % 2 == 0:
        return 1
    else:
        return -1




class Solution:
    def arraySign(self, nums: List[int]) -> int:
        return signFunc(nums)

