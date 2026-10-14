class Solution:
    def isPalindrome(self, s: str) -> bool:
        splitStr = "".join(c.lower() for c in s if c.isalnum())
        i, j = 0, len(splitStr) - 1
        while(i <=  j):
            if i == j:
                return True
            if splitStr[i] != splitStr[j]:
                return False
            i+=1
            j-=1
        return i > j