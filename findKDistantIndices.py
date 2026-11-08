class Solution:
    def findKDistantIndices(self, nums: list[int], key: int, k: int) -> list[int]:
        t=[]
        for i in range(len(nums)):
            if nums[i]==key:
                for j in range(len(nums)):
                    m= abs(j-i)
                    if m<=k:
                       t.append(j)
        return sorted(set(t))
