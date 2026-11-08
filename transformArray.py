class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        t=[]
        m=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                t.append(nums[i])
            else:
                m.append(nums[i])
        n=t+m
        a=[]
        for i in range(len(n)):
            if n[i]%2==0:
                a.append(0)
            else:
                a.append(1)
        return a
                

        
