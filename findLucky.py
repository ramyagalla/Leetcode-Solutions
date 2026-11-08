class Solution:
    def findLucky(self, arr: list[int]) -> int:
        freq={}
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        lucky=-1
        for i in freq:
            if freq[i]==i:
                lucky=max(lucky,i)
        return lucky
