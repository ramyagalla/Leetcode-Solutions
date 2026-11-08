class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        t=[]
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
                t.append(nums[i])
            else:
                t.append(nums[i])
        t.append(nums[-1])
        a=[]
        for i in range(len(t)):
            if t[i]!=0:
                a.append(t[i])
        a+=[0]*t.count(0)
        return a


