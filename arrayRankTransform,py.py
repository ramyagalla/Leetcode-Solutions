class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        s=sorted(set(arr))
        freq={}
        for i in range(len(s)):
            freq[s[i]]=i+1
        t=[]
        for i in arr:
            t.append(freq[i])
        return t
