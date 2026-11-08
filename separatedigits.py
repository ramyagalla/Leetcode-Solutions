class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        t=[]
        for i in nums:
            if i<=9:
                t.append(i)
            else:
                k=[]
                while i>0:
                    nums=i//10
                    k.append(i%10)
                    i=nums
                t.extend(k[::-1])
        return t


        
