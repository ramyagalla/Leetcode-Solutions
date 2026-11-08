class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if min(nums)<k:
            return -1
        t=set()
        for i in nums:
            if i>k:
                t.add(i)
            
        return len(t)
