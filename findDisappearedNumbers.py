class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        t=[]
        nums.sort()
        k=len(nums)
        for i in range(1,k+1):
            if i not in nums:
                t.append(i)
        return t
        
