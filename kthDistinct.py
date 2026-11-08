class Solution:
    def kthDistinct(self, arr: list[str], k: int) -> str:
        freq={}
        for i in arr:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        t=[]
        for i in arr:
            if freq[i]==1:
                t.append(i)
        if len(t)>=k:
            return t[k-1]
        else:
            return ""

            
        
