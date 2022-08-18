class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        long_arr = nums1 if len(nums1) > len(nums2) else nums2
        short_arr = nums2 if len(nums1) > len(nums2) else nums1
        result = []
        for i in short_arr:
            if i in long_arr:
                result.append(i)
                long_arr.remove(i)
        return result
