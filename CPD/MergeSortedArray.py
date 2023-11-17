class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1=0
        i2=0
        res=[]
        while i1 < m and i2 < n:
            if nums1[i1] <= nums2[i2]:
                res.append(nums1[i1])
                i1+=1
            else:
                res.append(nums2[i2])
                i2+=1
        res.extend(nums1[i1:m])
        res.extend(nums2[i2:n])

        for i in range(m+n):
            nums1[i] = res[i]

        """
        Do not return anything, modify nums1 in-place instead.
        """
        
