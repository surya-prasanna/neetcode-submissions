class Solution:
    def isPathCrossing(self, path: str) -> bool:
        currentpos = (0,0)
        prevMap = {currentpos}
        for direction in path:
            x, y = currentpos 
        
        
            if direction == 'N':
                currentpos = (x, y + 1)
            elif direction == 'S':
                currentpos = (x, y - 1)
            elif direction == 'E':
                currentpos = (x + 1, y)
            elif direction == 'W':
                currentpos = (x - 1, y)
            

            if currentpos in prevMap:
                return True

            prevMap.add(currentpos)
        return False 
        