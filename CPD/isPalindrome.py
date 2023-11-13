class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for l in s:
            if l.isalnum():
                res+=l
        return res.lower() == res[::-1].lower()
