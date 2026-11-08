class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            while nums[i]>=nums[i+1]  :
                nums[i+1]+=1
                c+=1
        return c

        
