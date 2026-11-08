class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatenation=0
        a=0
        if len(nums)==1:
            a+=nums[0]
            return a
        while len(nums)>1:
            m=nums[0]
            n=nums[-1]
            j=str(m)+str(n)
            k=int(j)
            concatenation+=k
            nums.pop(0)
            nums.pop()
            if len(nums)==1:
                concatenation+=nums[0]
        return concatenation

            
        
