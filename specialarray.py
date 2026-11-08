class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            t=[]
            t.append(nums[i])
            t.append(nums[i+1])
            if t[0]%2==0 and t[1]%2!=0:
                continue
            elif t[0]%2!=0 and t[1]%2==0:
                continue
            else:
                return False
        return True

