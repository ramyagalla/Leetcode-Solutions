class Solution:
    def isGood(self, nums: List[int]) -> bool:
        freq={}
        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]]=1
            else:
                freq[nums[i]]+=1
        m=max(nums)
        if freq[m]!=2:
            return False
        if len(nums)!=m+1:
            return False
        for i in range(1,m):
            if freq.get(i,0)!=1:
                return False
        return True
            
