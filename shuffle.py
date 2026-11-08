class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        m=[]
        a=[]
        for i in range(n):
            m.append(nums[i])
        for j in range(n,2*n):
            a.append(nums[j])
        t=[]
        i=0
        while i<n:
            t.append(m[i])
            t.append(a[i])
            i+=1
        return t

        
