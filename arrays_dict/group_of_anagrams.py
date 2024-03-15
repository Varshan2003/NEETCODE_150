class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for s in strs:
            st = tuple(sorted(s))  
            if st in map:
                map[st].append(s)
            else:
                map[st] = [s]
        ans = []
        for i in map:
            ans.append(map[i])
        return ans
