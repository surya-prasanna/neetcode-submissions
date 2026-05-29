class Solution:
    def isPalindrome(self, s: str) -> bool:
        char_list = [char.lower() for char in s if char.isalnum()]

        for i in range(round(len(char_list) / 2)):
            if char_list[i] != char_list[len(char_list) - i - 1]:
                return False
        return True


        