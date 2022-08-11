class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum=0
        maxResult = currSum = nums[0]
        for num in nums[1:]:
            currSum = max(currSum+num, num)
            maxResult= max(maxResult,currSum)
        print(maxResult)
        return maxResult
