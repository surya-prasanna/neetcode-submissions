class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mapStringPattern, mapPatternString = {}, {}
        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            c = pattern[i]
            word = words[i]

            if ((c in mapStringPattern and mapStringPattern[c] != word)
            or (word in mapPatternString and mapPatternString[word] != c)):
                return False

            mapStringPattern[c] = word
            mapPatternString[word] = c
        

        return True

        