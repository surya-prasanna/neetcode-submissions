class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)

        ans = 0
        isOne = False 


        for item in count: 
            if count[item] % 2 == 0: 
                ans += count[item]
            elif count[item] == 1:
                isOne = True
            else: 
                ans += count[item] - 1
                isOne = True
        
        if isOne:
            return ans + 1
        else:
            return ans