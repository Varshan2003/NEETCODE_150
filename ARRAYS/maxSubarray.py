class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        currSum = 0
        for num in nums:
            if currSum<0:
                currSum = 0
            currSum+=num
            ans = max(ans,currSum)
        return ans
