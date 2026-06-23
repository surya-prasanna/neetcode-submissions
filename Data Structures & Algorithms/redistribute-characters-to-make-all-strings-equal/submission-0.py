class Solution:
    def makeEqual(self, words: List[str]) -> bool:

        string = ""

        for word in words:
            string += word
        
        count = Counter(string)

        for item in count:
            if count[item] % len(words) != 0:
                return False


        return True        