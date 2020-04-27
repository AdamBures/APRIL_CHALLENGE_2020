class Solution:
    def countElements(self, arr: List[int]) -> int:
        setting = {}
        for i in arr:
            setting[i]=1

        result = 0
        for x in arr:
            if x+1 in setting:
                result +=1
        return result
