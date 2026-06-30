class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = j = 0

        while i < len(word) and j < len(abbr):
            if abbr[j] == '0':
                return False
            if abbr[j].isalpha():
                if word[i] != abbr[j]:
                    return False
                i, j = i + 1, j + 1
            else:
                first = j
                while j < len(abbr) and abbr[j].isdigit():
                    j += 1
                i += int(abbr[first:j])
                
        return j == len(abbr) and i == len(word)