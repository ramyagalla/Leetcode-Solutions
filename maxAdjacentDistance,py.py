class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        t=[]
        m=abs(nums[0]-nums[-1])
        t.append(m)
        for i in range(len(nums)-1):
            k=nums[i]-nums[i+1]
            t.append(abs(k))
        return max(t)
