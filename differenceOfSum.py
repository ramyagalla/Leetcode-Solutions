class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        s=0
        for i in nums:
            s+=i
        k=0
        for i in nums:
            if i<=9:
                k+=i
            else:
                m=[]
                while i>0:
                    nums=i//10
                    m.append(i%10)
                    i=nums
                for j in m:
                    k+=j
        return abs(s-k)

        
