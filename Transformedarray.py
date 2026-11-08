class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result=[]
        n=len(nums)
        for i in range(n):
            index=(i+nums[i]+n)%n
            result.append(nums[index])
        return result
           
