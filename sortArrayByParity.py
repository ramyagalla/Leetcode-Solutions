class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        a=[]
        b=[]
        for i in nums:
            if i%2==0:
                a.append(i)
            else:
                b.append(i)
        c=a+b
        return c


        
