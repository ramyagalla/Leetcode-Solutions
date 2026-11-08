class Solution:
    def relativeSortArrays(self, arr1: list[int], arr2: list[int]) -> list[int]:
        freq={}
        for i in arr1:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        t=[]
        a=[]
        for i in arr2:
                t.extend([i]*freq[i])
        for i in sorted(freq):
            if i not in arr2:
                a.extend([i]*freq[i])
        n=t+a
        return n
            
