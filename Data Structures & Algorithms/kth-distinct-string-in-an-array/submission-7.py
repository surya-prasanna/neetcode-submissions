class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        
        count = Counter(arr)
        x = 0

        for element, frequency in count.items():
            if frequency == 1:
                x += 1
                if x == k:
                    return element
        

        return ""
