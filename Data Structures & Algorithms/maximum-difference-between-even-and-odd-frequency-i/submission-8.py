class Solution:
    def maxDifference(self, s: str) -> int:
        char_map = Counter(s)

        even_min = float('inf')
        odd_max = 0

        for chars in char_map.values():
            if chars % 2 == 0:
                even_min = min(chars, even_min)
            else:
                odd_max = max(chars, odd_max)
        

        return odd_max - even_min if even_min != float('inf') else odd_max

        