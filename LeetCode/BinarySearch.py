class Solution:
    def search2(self, nums: List[int], target: int) -> int:
        if target in nums:
            index = nums.index(target)
            return index
        return -1
    
    def search(self,nums: List[int], target: int) -> int:
        #Assumption: nums list is always sorted in Ascending order
        low = 0
        high = len(nums)-1
        mid = 0
        
        while low<= high:
            mid = (low+high)//2
            
            if target > nums[mid]:
                low = mid+1
            elif target< nums[mid]:
                high = mid-1
            else:
                return mid
        return -1
