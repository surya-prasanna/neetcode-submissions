class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for word in words:
            good = True
            for chars in word:
                if chars not in allowed:
                    good = False
                    break
            if good:
                ans += 1
        return ans