class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevmap = {}
        for idx,value in enumerate(nums):
            diff = target-value
            if diff in prevmap:
                return [prevmap[diff],idx]
            prevmap[value] = idx
        return
        
