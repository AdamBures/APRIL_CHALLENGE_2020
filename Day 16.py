class Solution:
    def checkValidString(self, s: str) -> bool:
        if len(s) == 0 or s=="*":
            return True
        if len(s) == 1:
            return False

        left = 0
        for i in s:
            if i==")":
                left -= 1
            else:
                left += 1
            if left<0:
                return False
        if left == 0:
            return True
        right = 0
        for i in reversed(s):
            if i=="(":
                right -= 1
            else:
                right += 1
            if right<0:
                return False

        return True
    
            
