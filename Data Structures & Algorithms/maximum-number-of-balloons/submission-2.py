class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        mp = defaultdict(int)


        for chars in text:
            if chars in "balon":
                mp[chars] += 1
            
        if len(mp) < 5:
            return 0
        
        mp['l'] //= 2
        mp['o'] //=2

        return min(mp.values())
            

        