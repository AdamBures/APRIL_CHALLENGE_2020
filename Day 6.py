class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            x = "".join(sorted(i))
            if x in result:
                result[x].append(i)

            else:
                result[x] = [i]
        return list(result.values())
