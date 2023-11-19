class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ls = s.rfind(s[0])
        res =[]
        l = 0
        if ls == 0:
            res.append(1)
            l+=1
        for i in range(1,len(s)):
            cur = s.rfind(s[i])
            if cur > ls:
                ls = cur
            if i == ls:
                res.append(i-l+1)
                l=i+1
        return res
