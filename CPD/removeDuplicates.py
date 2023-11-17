class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums2 = list(set(nums))
        nums2.sort()
        nums[:len(nums2)] = nums2
        return len(nums2)
            
