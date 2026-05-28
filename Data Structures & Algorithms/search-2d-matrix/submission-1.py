class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = []
        for sublist in matrix:
            for item in sublist:
                flat_list.append(item)

        low = 0
        high = len(flat_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if flat_list[mid] == target:
                return True
            elif flat_list[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False


        