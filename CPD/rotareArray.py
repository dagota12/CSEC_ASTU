class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = k%len(nums) 
        nums[:n],nums[n:] = nums[len(nums) - n:],nums[:len(nums) - n]
        """
        Do not return anything, modify nums in-place instead.
        """
        
