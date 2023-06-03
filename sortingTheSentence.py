class Solution:
    def sortSentence(self, s: str) -> str:
        def based(elem):
            return elem[1]
        words = [[txt[0:-1],int(txt[-1])] for  txt in s.strip().split(" ")]
        words.sort(key=based)
        return (" ".join(txt[0] for txt in words))
