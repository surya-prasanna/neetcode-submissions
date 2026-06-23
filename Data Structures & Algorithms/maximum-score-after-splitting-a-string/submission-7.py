class Solution:
    def maxScore(self, s: str) -> int:
        res =0

        for i in range(1, len(s)):
            
            substring1 = s[0:i]
            substring2 = s[i:len(s)]

            count1 = Counter(substring1)
            count2 = Counter(substring2)

            score = count1["0"] + count2["1"]
        
            res = max(score, res)
        return res