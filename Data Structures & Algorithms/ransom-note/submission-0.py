class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        magazine_count = Counter(magazine)


        for chars in ransom_count:
            if ransom_count[chars] > magazine_count[chars]:
                return False
        

        return True