class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        orderd = sorted(nums)
        count =[]
        i = 0 
        for n in nums:
            while orderd[i] < n and i<len(nums):
                i+=1
            count.append(i)
            i=0
        return count
