class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        length = -1
        for i in range(len(s) - 1):
            if s[i] in s[i:]:
                length = max(length, s.rfind(s[i]) - i - 1)
        return length

        