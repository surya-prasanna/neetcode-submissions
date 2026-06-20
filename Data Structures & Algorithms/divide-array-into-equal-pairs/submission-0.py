class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        count = Counter(nums)
        numbers = list(set(nums))

        for i in range(len(count)):
            if count[i] % 2 != 0:
                return False
        return True

        