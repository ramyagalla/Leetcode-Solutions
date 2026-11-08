class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        m=""
        n=""
        for i in word1:
            m+=i
        for i in word2:
            n+=i
        if m==n:
            return True
        else:
            return False
