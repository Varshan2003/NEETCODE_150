class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return list(set(nums))!=nums
        
