class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr.sort(reverse=True)

        freq_map = Counter(arr)

        for freq in freq_map:
            if freq_map[freq] == freq:
                return freq
        return -1

