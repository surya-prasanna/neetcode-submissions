class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in ans: 
                ans[sorted_word] = []
            ans[sorted_word].append(word)
        
        return list(ans.values())
