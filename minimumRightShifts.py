class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        c=0
        n=len(nums)
        for i in range(n):
            if nums[i]>nums[(i+1)%n]:
                c+=1
                ans=n-i-1
        if c==1:
            return ans
        if c==0:
            return 0
        return -1

        
