class Solution:
    def minOperations(self, s: str) -> int:
        pattern1 = 0
        pattern2 = 0 

        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    pattern1 += 1
            else: 
                if s[i] != '1':
                    pattern1 += 1


            if i % 2 == 0:
                if s[i] != '1':
                    pattern2 += 1
            else:
                if s[i] != '0':
                    pattern2 += 1
        
        return min(pattern1, pattern2)

                







        

            