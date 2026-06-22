class Solution:
    def largestGoodInteger(self, num: str) -> str:

        runningTotal = 1
        ans = ""

        for i in range(1, len(num)):
            if num[i] == num[i - 1]:
                runningTotal += 1
                if runningTotal == 3:
                    runningTotal = 1
                    candidate = num[i] * 3
                    if candidate > ans:
                        ans = candidate

            else:
                runningTotal = 1





        return ans
        