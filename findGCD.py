class Solution:
    def findGCD(self, nums: list[int]) -> int:
        m=min(nums)
        n=max(nums)
        t=[]
        k=[]
        for i in range(1,m+1):
            if m%i==0:
                t.append(i)
        for i in range(1,n+1):
            if n%i==0:
                k.append(i)
        l=set(t).intersection(set(k))
        return max(l) 
        
